text = "X-DSPAM-Confidence:    0.8475";
t = text.replace("    ", "")
startPos = t.find(':')
print(t[startPos+1:])