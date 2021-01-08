from cx_Freeze import setup , Executable
setup(name = "Riddles Quiz",
        version = "1.0",
        author = "Parth Soni",
        description = "This quiz is related to riddles where you have to answer the riddle quesions",
        executables = [Executable(r"C:\Users\Hp\Desktop\New folder\quiz\riddles quiz.py",
                                                      icon = r"C:\Users\Hp\Desktop\New folder\quiz\Education.ico",
                                                     shortcutName="Riddles Quiz",
                                                     shortcutDir="DesktopFolder")]
                                  
   )
