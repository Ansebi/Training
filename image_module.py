def congrats():
    print("              ")
    print("              ")
    print("     **   **  ")
    print("     **   **  ")
    print("              ")
    print("   *         *")
    print("    *       * ")
    print("     *******  ")
    print("       ***    ")
    print("              ")



def lose():
    print("              ")
    print("    * *   * * ")
    print("     *     *  ")
    print("    * *   * * ")
    print("              ")
    print("              ")
    print("     *******  ")
    print("    *       * ")
    print("   *         *")
    print("              ")



def numeric_display(score):
    digit=[
    [" ** ","*  *","*  *","*  *"," ** "],
    ["   *","  **","   *","   *","   *"],
    [" ** ","*  *","  * "," *  ","****"],
    [" ** ","*  *","  * ","*  *"," ** "],
    ["*  *","*  *","****","   *","   *"],
    ["****","*   ","*** ","   *","*** "],
    [" ***","*   ","****","*  *","****"],
    ["****","   *","  * "," *  ","*   "],
    [" ** ","*  *"," ** ","*  *"," ** "],
    ["****","*  *","****","   *","*** "]
    ]

    score=str(score)
    for i in range(len(digit[0])):    
        row=[]
        for counter in range(len(score)):
            row.append(digit[int(score[counter])][i])        
        row=" ".join(row)
        print(row)
