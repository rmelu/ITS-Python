destinazioni = ["New York","Parigi","Turchia","Berlino","Islanda"]
print("ordine originale:", destinazioni)
print("ordine alfabetico:", sorted(destinazioni))
print("ordine originale (di nuovo):", destinazioni)
print("ordine alfabetico inverso:",sorted(destinazioni,reverse=True))
print("ordine originale(di nuovo):", destinazioni)
destinazioni.reverse()
print("ordine invertito:", destinazioni)
destinazioni.reverse()
print("ordine originale (di nuovo):", destinazioni)
destinazioni.sort()
print("ordinato alfabeticamente:", destinazioni)
destinazioni.sort(reverse=True)
print("ordinato alfabeticamente al contrario:", destinazioni)

