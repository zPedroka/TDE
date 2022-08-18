preço=float(input("qual é o preço"))
jurosParc=preço*1.05
parcela1=(jurosParc/3)
parcela2=(preço/2)
aVista=preço/1.05
print(" Em caso de 3 parcelas "+str(parcela1) + " Em caso de 2 parcelas "+str(parcela2)+ " Em caso do pagamento a vista "+str(aVista))