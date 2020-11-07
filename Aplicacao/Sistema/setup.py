from cx_Freeze import setup, Executable

setup(
        name = "MoneyMS",
        version = "0.9",
        description = "Investimentos Financeiros",
        executables = [Executable('MoneyMS.py', base = "Win32GUI", icon = "icone_janela.ico")])