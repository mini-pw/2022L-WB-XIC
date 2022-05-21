def train(model, criterion, optimizer, zero_epoch, epochs, train_loader, test_loader, DEVICE, train_acc=[], test_acc=[]):
    
    for epoch in range(epochs):
        correct_train = 0
        for batch in train_loader:     
            images = batch[0].to(DEVICE)
            labels = batch[1].to(DEVICE)
            preds = model(images)
            loss = criterion(preds, labels)
    
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
    
            _, predicted = preds.max(1)
    
            correct_train += predicted.eq(labels).sum().item()
    
        accuracy_train = correct_train / len(train_loader.dataset)
        train_acc.append(accuracy_train)
    
        # test
        correct_test = 0
    
        for batch in test_loader:     
            images = batch[0].to(DEVICE)
            labels = batch[1].to(DEVICE)
            preds = model(images)
            _, predicted = preds.max(1)
            correct_test += predicted.eq(labels).sum().item()
    
        accuracy_test = correct_test / len(test_loader.dataset)
        test_acc.append(accuracy_test)
    
        print(f"Epoch: {zero_epoch + epoch}, train accuracy: {accuracy_train}, test accuracy: {accuracy_test}")
        
    return train_acc, test_acc
