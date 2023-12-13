import matplotlib.pyplot as plt

from sklearn.datasets import fetch_lfw_people
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.decomposition import PCA as RandomizedPCA
from sklearn.pipeline import make_pipeline
from sklearn.metrics import accuracy_score

from colorama import Fore
from sklearn.metrics import classification_report

faces = fetch_lfw_people(min_faces_per_person=60)
fig, splts = plt.subplots(2, 4)

for i, splts in enumerate(splts.flat):
    splts.imshow(faces.images[i], cmap='magma')
    splts.set(xticks=[], yticks=[],
            xlabel=faces.target_names[faces.target[i]])

X = faces.data
y = faces.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=42)

pca = RandomizedPCA(n_components=150, whiten=True, random_state=42)
svc = SVC(kernel='rbf', class_weight='balanced')
model = make_pipeline(pca, svc)

model.fit(X_train, y_train)

predictions = model.predict(X_test)

print(accuracy_score(predictions, y_test))

incorrect = 0

length = len(predictions)

print("Actual\t\t\t\tPredicted\n")

for i in range(len(predictions)):
    if predictions[i] != y_test[i]: # if predictions and actual values are not equal
        prediction_name = faces.target_names[predictions[predictions[i]]] # Getting the predicted name
        actual_name = faces.target_names[y_test[y_test[i]]] # Getting the actual name
        incorrect+=1 
        print("{}\t\t\t{}".format(Fore.GREEN + actual_name, Fore.RED+prediction_name))
        
print("{} are classified as correct and {} are classified as incorrect!".format(length-incorrect, incorrect))

print(classification_report(predictions, y_test, digits=2))