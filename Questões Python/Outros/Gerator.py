"""
def tabuada(num):
    for i in range(1,21):
        calc = num*i
        print(num, "x" ,i, "=", calc)
num = int(input("Mande um número:"))
print(tabuada(num))
|---------------------------------------------------------------------------------------------------|

import random
import string
import tkinter as tk
from tkinter import messagebox
def gerador(tamanho):
    carac= string.ascii_letters + string.ascii_uppercase + string.digits + string.ascii_lowercase
    senha=''.join(random.choice(carac) for _ in range(tamanho))
    return senha
tamanho = int(input("Tamanho da sua senha: "))
senha = gerador(tamanho)
print(f"sua senha é {senha}")
usuary=int(input("Escolha seu nome de usuário: "))
|--------------------------------------------------------------------------------------------------|
import random

def login(name1):
    especi=[".",";","_","__","$","*","@","~"]
    match ape:
        case "administracão":
            lista =["AdminAce","Controll","SysSover","Networker","Commander","RootRuler","Adept","Sentinel","Sovereign","ConfigKing","TechTitan","Accessrul","CommandCon","NetNavi", "Admin"]
            digi= random.choice(especi) + random.choice(especi)
            nicks = [name1 + digi + nick for nick in lista]
            return nicks
        case "infoweb":
            lista =["CodeWarrior","ByteMaster","TechSavant","CyberNinja","BitCrafter","DataGuru" ,"NetWizard","ScriptSage","SystemShaman","AlgoArchitect", "QuantumCoder","HackHero" ,"TechieTactician", "ServerScribe", "LogicLancer"]
            digi= random.choice(especi) + random.choice(especi)
            nicks =[name1 + digi + nick for nick in lista]
            return nicks
        case "eletrotécnica":
            lista =["Volter","Current", "CircuitSage" ,"PowerGuru", "WattWhiz", "Electro", "SparkMaster" ,"AmpArchitect", "Resistor","Conductor", "Energys", "ChargeChamp","OhmOracle", "PowerPalad" ,"ElecEnth"]
            digi= random.choice(especi) + random.choice(especi)
            nicks =[name1 + digi + nick for nick in lista]
            return nicks
        case "manutenção":
            lista =["TechTroub","SupportSag" ,"FixItGu", "ITRescueRan", "SystemSav", "TechWhis","supporTprfs", "ITFixer" ,"HelpDesker", "MSItech", "TechMed", "SysStrat", "Trublshoot" ,"TecherAce","RepairRa"]
            digi= random.choice(especi) + random.choice(especi)
            nicks =[name1 + digi + nick for nick in lista]
            return nicks
        case "controle ambiental":
            lista =["EcoGuard","GreenGenius", "SustainX", "EcoSent", "GreenVibe"," TerraTech", "EcoStar", "GreenAce", "EnviroPro", "EcoRex"]
            digi= random.choice(especi) + random.choice(especi)
            nicks =[name1 + digi + nick for nick in lista]
            return nicks
        case "mineração":
            lista = ["MineMaster","RockRanger","OreGuru", "DigTech", "MineXpert","RockHound", "OreAce", "DigWizard", "MineMaven", "QuarryKing"]
            digi= random.choice(especi) + random.choice(especi)
            nicks =[name1 + digi + nick for nick in lista]
            return nicks
        case "geologia":
            lista = ["GeoGuru", "RockDoc", "EarthAce", "GeoMaven", "RockXpert", "TerraWhiz", "GeoRanger", "StoneSavvy", "EarthNerd", "RockStar"]
            digi= random.choice(especi) + random.choice(especi)
            nicks =[name1 + digi + nick for nick in lista]
            return nicks
        case "edificações":
            lista = ["BuildMaster", "StructGuru", "ArchAce", "BuildXpert","EdificePro", "ConstrX", "ArchWhiz", "BuildRex", "StructMaven", "EdifyTech"]
            digi= random.choice(especi) + random.choice(especi)
            nicks =[name1 + digi + nick for nick in lista]
            return nicks
        case "mecânica":
            lista = ["MechMaster", "GearGuru", "AutoAce", "MechWhiz", "GearXpert", "MechRex", "FixTech", "TorquePro", "MechMaven", "AutoSavvy"]
            digi= random.choice(especi) + random.choice(especi)
            nicks =[name1 + digi + nick for nick in lista]
            return nicks
    #gap = name1 + digi + ape
print("Mande um nome ou uma abreviação de seu nome:")
name1=input()
print("Por motivos para criação de username, qual curso do IFRN CNAT que você gosta mais? ")
ape = input().strip()
suggestions = login(name1)
print("Sugestões de nicks:")
for suggestion in suggestions:
    print("-----------------------")
    print(suggestion)
|--------------------------------------------------------------------------------------------------|
"""
