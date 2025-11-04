# mood_tracker.py
import necessaryFunction as nf

def main():
    while True:
        nf.load()
        mood = input('\nBagaimana mood kalian hari ini? (ketik "0" untuk keluar): ')
        
        if mood == '0':
            nf.clear()
            print("Terima kasih telah menggunakan Mood Tracker! 😊")
            break
        
        print(f"\nMood kamu: {mood}")
        nf.delayInput()
        nf.clear()

if __name__ == "__main__":
    main()