import os, sys

def determina_path():
    root=__file__
    if os.path.islink(root):
        root = os.path.realpath(root)

    return os.path.dirname(os.path.abspath(root))

def comezo():
    print("O modulo está funcionando")
    print(determina_path())
    print("Meus ficheiros e datos están en:")
    files = [f for f in os.listdir(determina_path() + "/cousas")]
    print(files)

if __name__=="__main__":
    print("Definir o que ten que faer o módulo si se executa directamente")