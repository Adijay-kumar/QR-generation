import qrcode

count = 0

while True:

    repo_url = input("Enter the github repo link : ")
    if repo_url == "done":
        break
    else:
        qr = qrcode.make(repo_url)
        file_name = f"project_qr_{count}.png"
        qr.save(file_name)
        print(file_name , "created succesfully")
        count += 1
