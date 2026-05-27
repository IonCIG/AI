from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

iris = load_iris()
X = iris.data
y = iris.target

print("Forma setului de date:", X.shape)
print("atribute", iris.feature_names)
print("clase", iris.target_names)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)
Scaler=StandardScaler()
X_train_scaled=Scaler.fit_transform(X_train)
X_test_scaled=Scaler.transform(X_test)
print("Forma setului de antrenare:", X_train.shape)
print("Forma setului de test:", X_test.shape)
print("Clases antrenare:", y_train.shape)
print("Clases test:", y_test.shape)
print("Setul de date scalat (antrenare):", X_train_scaled)
print("Setul de date scalat (test):", X_test_scaled)
print("Setul de date original (antrenare):", X_train[:5])
print(X_train_scaled[:5])
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train_scaled, y_train)
accuracy = knn.score(X_test_scaled, y_test)
print("Acuratețea modelului:", accuracy)



if __name__ == "__main__":
    import matplotlib.pyplot as plt

    k_values = list(range(1, 16))
    accuracies = []

    for k in k_values:
        knn_k = KNeighborsClassifier(n_neighbors=k)
        knn_k.fit(X_train_scaled, y_train)
        score_k = knn_k.score(X_test_scaled, y_test)
        accuracies.append(score_k)
        print(f"k={k}: acuratețe={score_k:.4f}")

    plt.figure(figsize=(8, 5))
    plt.plot(k_values, accuracies, marker='o', linestyle='-')
    plt.title('Acuratețea KNN în funcție de k')
    plt.xlabel('k')
    plt.ylabel('Acuratețe')
    plt.xticks(k_values)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('knn_accuracy_k.png')
    print("Graficul a fost salvat în: knn_accuracy_k.png")

    best_accuracy = max(accuracies)
    best_ks = [k for k, acc in zip(k_values, accuracies) if acc == best_accuracy]
    print(f"Cea mai bună acuratețe: {best_accuracy:.4f} pentru k={best_ks}")

    from sklearn.metrics import confusion_matrix, classification_report

    y_pred = knn.predict(X_test_scaled)
    cm = confusion_matrix(y_test, y_pred)
    report = classification_report(y_test, y_pred, target_names=iris.target_names)

    print("\nMatrice de confuzie:")
    print(cm)
    print("\nRaport de clasificare:")
    print(report)

    print("\nVizualizare scatter cu 2 caracteristici (petal length și petal width):")
    X_2d = X[:, [2, 3]]
    X_train_2d = X_train[:, [2, 3]]
    X_test_2d = X_test[:, [2, 3]]

    scaler_2d = StandardScaler()
    X_train_2d_scaled = scaler_2d.fit_transform(X_train_2d)
    X_test_2d_scaled = scaler_2d.transform(X_test_2d)

    knn_2d = KNeighborsClassifier(n_neighbors=3)
    knn_2d.fit(X_train_2d_scaled, y_train)

    plt.figure(figsize=(8, 5))
    colors = ["red", "green", "blue"]
    for class_idx, class_name in enumerate(iris.target_names):
        mask = y == class_idx
        plt.scatter(X_2d[mask, 0], X_2d[mask, 1], color=colors[class_idx], label=class_name, edgecolor='k', alpha=0.8)

    plt.xlabel("Petal length (cm)")
    plt.ylabel("Petal width (cm)")
    plt.title("Iris scatter: lungime vs lățime petală")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('iris_scatter_2features.png')
    print("Graficul scatter a fost salvat în: iris_scatter_2features.png")

    print("\nSimulare predicție pentru o floare nouă:")
    try:
        pl = float(input("Introduceți lungimea petalei (cm): "))
        pw = float(input("Introduceți lățimea petalei (cm): "))
        sample = [[pl, pw]]
        sample_scaled = scaler_2d.transform(sample)
        pred = knn_2d.predict(sample_scaled)[0]
        print(f"Predicția modelului KNN: {iris.target_names[pred]}")
    except ValueError:
        print("Valori invalide: introduceți numere reale pentru lungime și lățime.")
    except Exception as e:
        print("Eroare la predicție:", e)
