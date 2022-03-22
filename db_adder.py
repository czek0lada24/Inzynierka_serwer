import db_com

if __name__ == "__main__":
    db_com.init()
    file_handler=open("products.txt", "r", encoding="UTF-8") #otwieramy plik txt do trybu read
    lines=file_handler.readlines()
    for line in lines:
        tmp=line.split(";")
        tmp[2]=tmp[2].rstrip()
        db_com.insert_product(tmp[0],tmp[1],tmp[2])

