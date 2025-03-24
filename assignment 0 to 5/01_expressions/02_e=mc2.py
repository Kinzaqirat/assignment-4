def main():
    mass=float(input("Enter Mass in kg: "))
    C: int = 299792458
    e = mass *( C**2)
    print(f"Energy = {e} joules of energy")



if __name__ == '__main__':
    main()