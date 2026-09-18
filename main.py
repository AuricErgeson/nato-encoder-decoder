from utils import encoder,decoder

print("""
<< To encode avoid using anything that is not letters, avoid using characters to shorten the words like (let's) >>
<< To decode words are separated by a space >>
    """)


def main():
    while True:
        choices = input("Enter your choice\n1.(To encode), 2.(To decode), 3.(To Exit):")
        if choices == "1":
            message = input("Enter your message: ")
            encoder(message)
        elif choices == "2":
            message = input("Enter your message: ")
            decoder(message)
        elif choices == "3":
            break

if __name__ == '__main__':
    main()