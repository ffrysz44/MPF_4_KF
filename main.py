def calfp(frates, fac_rate):
    # Tablice z nazwami (zostają zachowane dla spójności z oryginałem, 
    # choć nie są bezpośrednio używane w obliczeniach)
    fun_units = [
        "External Inputs",
        "External Outputs",
        "External Inquiries",
        "Internal Logical Files",
        "External Interface Files"
    ]
    
    wt_rates = ["Low", "Average", "High"]

    # Wagi (Weight Factors)
    wt_factors = [
        [3, 4, 6],
        [4, 5, 7],
        [3, 4, 6],
        [7, 10, 15],
        [5, 7, 10]
    ]

    ufp = 0

    # Obliczanie UFP (Unadjusted Function Point)
    for i in range(5):
        for j in range(3):
            freq = frates[i][j]
            ufp += freq * wt_factors[i][j]

    # 14 czynników wpływających na złożoność
    aspects = [
        "reliable backup and recovery required ?",
        "data communication required ?",
        "are there distributed processing functions ?",
        "is performance critical ?",
        "will the system run in an existing heavily utilized operational environment ?",
        "on line data entry required ?",
        "does the on line data entry require the input transaction to be built over multiple screens or operations ?",
        "are the master files updated on line ?",
        "is the inputs, outputs, files or inquiries complex ?",
        "is the internal processing complex ?",
        "is the code designed to be reusable ?",
        "are the conversion and installation included in the design ?",
        "is the system designed for multiple installations in different organizations ?",
        "is the application designed to facilitate change and ease of use by the user ?"
    ]

    # Obliczanie sumy czynników (zastępuje pętlę for z C++)
    sum_f = fac_rate * 14

    # Obliczanie CAF (Value Adjustment Factor / Complexity Adjustment Factor)
    caf = 0.65 + 0.01 * sum_f

    # Obliczanie ostatecznej wartości Function Point (FP)
    fp = ufp * caf

    # Wypisywanie wyników
    print("Function Point Analysis :-")
    print(f"Unadjusted Function Points (UFP) : {ufp}")
    print(f"Complexity Adjustment Factor (CAF) : {caf:.2f}")
    print(f"Function Points (FP) : {fp:.2f}")


# Funkcja główna (odpowiednik int main())
if __name__ == "__main__":
    frates = [
        [0, 1, 0],
        [0, 1, 0],
        [0, 3, 0],
        [0, 1, 0],
        [0, 3, 0]
    ]

    fac_rate = 2

    calfp(frates, fac_rate)
