
import cv2
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np
from scipy.spatial import cKDTree as KDTree
from skimage.draw import polygon, disk


class ImageDetails:
    def __init__(self, image=None):
        self._update_image(image)
        self.small_figure_shapes_counts = {}
        self.color_names_matrix = None
        self.plot = False
        self.plots = {}

    def _set_tresholds(self): # parameters found by grid search on 1296 figures (432 of each shape)
        if self.original_img_shape == (600,600): # accuracy around 0.7
            self.small_shapes_thresholds = {
                "square":[0.017],
                "triangle":[0.11,0.15],
                "circle":{"dp":1.2, "minDist":8, "param1":100, "param2":20, "maxRadius":20,"minRadius":1}
            }
        elif self.original_img_shape == (256,256): # accuracy around 0.75 
            self.small_shapes_thresholds = {
                "square":[0.045],
                "triangle":[0.11, 0.13],
                "circle":{"dp":1.2, "minDist":4, "param1":400, "param2":16, "maxRadius":9,"minRadius":2}
            }

    def _update_image(self, image):
        if image is not None:
            self.original_image = cv2.cvtColor(image.permute(1,2,0).numpy(), cv2.COLOR_RGB2BGR)
            self.original_img_shape = self.original_image.shape[:2]
            self._set_tresholds()

    def get_colors_matrix(self, image=None): # return matrix with every pixel as code 0,1,2,3,4
        self._update_image(image)       
        # codes = {0: 'red', 1: 'yellow', 2: 'blue', 3:"gray", 4:"unknown"}
        # source: https://stackoverflow.com/questions/50545192/count-different-colour-pixels-python
        use_colors = {k: colors.cnames[k] for k in ['red', 'yellow', 'blue', 'gray', 'purple']}
        named_colors = {k: tuple(map(int, (v[1:3], v[3:5], v[5:7]), 3*(16,))) for k, v in use_colors.items()}
        ncol = len(named_colors)

        color_tuples = list(named_colors.values())
        color_tuples.append(named_colors.pop('purple'))
        color_tuples = np.array(color_tuples)

        color_names = list(named_colors)
        color_names.append('no match')

        img = cv2.cvtColor(self.original_image, cv2.COLOR_BGR2RGB) * 255

        tree = KDTree(color_tuples[:-1])
        dist, idx = tree.query(img, distance_upper_bound=np.inf)
        return idx

    def get_color_names_matrix(self, image=None): # return matrix with every pixel as string "color_name"
        self._update_image(image)       
        idx = self.get_colors_matrix()
        codes = {0: 'red', 1: 'yellow', 2: 'blue', 3:"gray", 4:"unknown"}
        pixel_colors = np.asarray(list(codes.values()))[idx]
        return pixel_colors  

    def _remove_colors(self):
        pixel_colors = self.get_color_names_matrix()
        zero_one_img = np.zeros(pixel_colors.shape)
        zero_one_img[pixel_colors != 'gray'] = 1
        zero_one_img = (zero_one_img*255).astype(np.uint8)
        return zero_one_img

    def _search_for_small_figures(self):
        # https://stackoverflow.com/questions/46300244/triangle-detection-using-opencv
        # https://www.thepythoncode.com/article/detect-shapes-hough-transform-opencv-python

        image_obj = self.original_image
        gray = self._remove_colors() 

        kernel = np.ones((4, 4), np.uint8)
        dilation = cv2.dilate(gray, kernel, iterations=1)

        blur = cv2.GaussianBlur(dilation, (5, 5), 0)
        thresh = cv2.adaptiveThreshold(blur, 255, 1, 1, 11, 2)

        # contours for triangles and squares
        if self.original_img_shape == (600,600):
            contours, _ = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        elif self.original_img_shape == (256,256):
            contours, _ = cv2.findContours(gray, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

        triangles = []
        squares = []
        
        clear_for_plots = np.ones(image_obj.shape) * 255 # for plots
        clear_for_plots = clear_for_plots.astype(np.int32) # for plots

        # selecting triangles, then squares //
        for cnt in contours:
            # [point_x, point_y, width, height] = cv2.boundingRect(cnt) #might be useful

            # 2 different "approx" because sometimes one of them selects circles/squares
            vertices_counts = [len(cv2.approxPolyDP(cnt, eps_triangle * cv2.arcLength(cnt, True), True)) for eps_triangle in self.small_shapes_thresholds["triangle"]]
            if all(np.array(vertices_counts) == 3):
                triangles.append(cnt)
                cv2.drawContours(clear_for_plots, [cnt], 0, (51, 102, 255), -1) # for plots
            else: 
                vertices_counts = [len(cv2.approxPolyDP(cnt, eps_square * cv2.arcLength(cnt, True), True)) for eps_square in self.small_shapes_thresholds["square"]]
                if all(np.array(vertices_counts) == 4):
                    squares.append(cnt)
                    cv2.drawContours(clear_for_plots, [cnt], 0, (0, 153, 0), -1) # for plots

        # selecting circles // [ [[x,y,r], [x,y,r], ...] ]
        # select more circles = decrease param2, increase dp 
        circles = cv2.HoughCircles(image=blur, method=cv2.HOUGH_GRADIENT, **self.small_shapes_thresholds["circle"])
        if circles is not None:
            circles = circles.astype(int)
            for x,y,r in circles[0,:]:
                cv2.circle(clear_for_plots,(x,y),r,(255, 51, 153),-1) # for plots

        self.plots["gray"] = gray
        self.plots["dilation"] = dilation
        self.plots["blur"] = blur
        self.plots["thresh"] = thresh
        self.plots["clear_for_plots"] = clear_for_plots
        
        if circles is not None:
            circles_count = len(circles[0])
        else: 
            circles_count = 0
        self.small_figure_shapes_counts = {"circles": circles_count,
                                            "triangles":len(triangles),
                                            "squares":len(squares)}

        return {"circles": circles,"triangles":triangles,"squares":squares}
    
    def get_shapes_and_figure_ids_matrices(self, image=None, raw=False):
        self._update_image(image)       
        # https://stackoverflow.com/questions/37117878/generating-a-filled-polygon-inside-a-numpy-array
        # https://scikit-image.org/docs/stable/auto_examples/edges/plot_shapes.html#sphx-glr-auto-examples-edges-plot-shapes-py
        shapes = {0: 'empty', 1: 'square', 2: 'triangle', 3:"circle"}
        keys_of_shapes = {v:k for k, v in shapes.items()}

        small_figures = self._search_for_small_figures()
        shapes_matrix = np.zeros(self.original_img_shape, dtype=np.uint8) 
        figure_ids_matrix = np.zeros(self.original_img_shape) - 1 # background is not a figure
        
        figures_counter = 1 # also as new ids
        for square in small_figures["squares"]:
            square = square.squeeze() # coords
            rr, cc = polygon(square[:,0], square[:,1], self.original_img_shape)
            shapes_matrix[rr,cc] = keys_of_shapes["square"]
            figure_ids_matrix[rr,cc] = figures_counter
            figures_counter += 1

        for triangle in small_figures["triangles"]:
            triangle = triangle.squeeze() # coords
            rr, cc = polygon(triangle[:,0], triangle[:,1], self.original_img_shape)
            shapes_matrix[rr,cc] = keys_of_shapes["triangle"]
            figure_ids_matrix[rr,cc] = figures_counter
            figures_counter += 1
        if small_figures["circles"] is not None:
            for circle in small_figures["circles"][0]:
                rr, cc = disk((circle[0], circle[1]), circle[2], shape=self.original_img_shape)
                shapes_matrix[rr, cc] = keys_of_shapes["circle"]
                figure_ids_matrix[rr,cc] = figures_counter
                figures_counter += 1

        if not raw:
            shape_names_matrix = np.asarray(list(shapes.values()))[shapes_matrix]
        else:
            shape_names_matrix = shapes_matrix
        return {"shape_names":shape_names_matrix.T,
                "figure_ids": figure_ids_matrix.T}

    def get_shapes_matrix(self, image=None, raw=False): # return matrix with every pixel as string "shape_name"
        self._update_image(image)       
        return self.get_shapes_and_figure_ids_matrices(raw=raw)["shape_names"]

    def get_small_figure_ids(self, image=None): # return matrix with every pixel as number "figure_id", -1 for background
        self._update_image(image)       
        return self.get_shapes_and_figure_ids_matrices()["figure_ids"]

    def _unify_shapes_between_matrices(self):
        self.shape_names_matrix[self.color_names_matrix == "gray"] = "empty"
        self.figure_ids_matrix[self.color_names_matrix == "gray"] = -1
        self.color_names_matrix[self.figure_ids_matrix == -1 ] == "gray"
        self.plots["clear_for_plots"][self.color_names_matrix == "gray"] = 255 


    def analyze(self, image=None, show_output=True, plot=False):
        self.plot=plot
        self._update_image(image)       
        shape_and_ids = self.get_shapes_and_figure_ids_matrices()
        self.shape_names_matrix = shape_and_ids["shape_names"]
        self.figure_ids_matrix = shape_and_ids["figure_ids"]
        self.color_names_matrix = self.get_color_names_matrix()

        self._unify_shapes_between_matrices()

        if self.plot:
            self.visualize()

        if show_output:
            return {"color_names":self.color_names_matrix,
                    "shape_names":self.shape_names_matrix,
                    "figure_ids": self.figure_ids_matrix}

    def pixel_analysis(self,x,y, image=None):
        if image is not None:
            self.analyze(image=image,show_output=False)
        return {"color_names":self.color_names_matrix[x,y],
                "shape_names":self.shape_names_matrix[x,y],
                "figure_ids": self.figure_ids_matrix[x,y]}

    def visualize(self):
        fig, ax = plt.subplots(2,3,figsize=(12,8))
        plt.suptitle("Figures detection pipeline", fontsize=20, y=0.97)
        ax[0][0].set_title("Input image")
        ax[0][0].imshow(cv2.cvtColor(self.original_image, cv2.COLOR_BGR2RGB))
        ax[0][1].set_title("After removing colors")
        ax[0][1].imshow(self.plots["gray"], cmap='Greys')
        ax[0][2].set_title("After dilation")
        ax[0][2].imshow(self.plots["dilation"], cmap='Greys')
        ax[1][0].set_title("After Gaussian Blur")
        ax[1][0].imshow(self.plots["blur"], cmap='Greys')
        ax[1][1].set_title("After Threshold")
        ax[1][1].imshow(self.plots["thresh"],cmap='Greys')
        ax[1][2].set_title("Result - figures found")
        ax[1][2].imshow(self.plots["clear_for_plots"])
        plt.show()

