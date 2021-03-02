import re
n = open('final_name.txt','r',encoding='utf-8')
name = n.read().split()
n.close()
for n in name:
	a = open('lyrics/'+n+'.txt','r',encoding='utf-8')
	f = a.read()
	a.close()
	o = open('chinese/'+n+'.txt','w',encoding='utf8')
	cc = open('roma/'+n+'.txt','w',encoding='utf8')
	final = open('final/'+n+'.txt','w',encoding='utf8')

	f = f.replace('á','a2').replace('à','a3').replace('â','a5').replace('ǎ','a6').replace('ā','a7').replace(u'\u030D','8')
	f = f.replace('é','e2').replace('è','e3').replace('ê','e5').replace('ě','e6').replace('ē','e7')
	f = f.replace('í','i2').replace('ì','i3').replace('î','i5').replace('ǐ','i6').replace('ī','i7')
	f = f.replace('ó','o2').replace('ò','o3').replace('ô','o5').replace('ǒ','o6').replace('ō','o7')
	f = f.replace('ú','u2').replace('ù','u3').replace('û','u5').replace('ǔ','u6').replace('ū','u7')
	f = f.replace(u'\u0300','3').replace(u'\u0302','5').replace(u'\u030C','6').replace(u'\u0304','7')

	rom = re.findall(u'([\u0020-\u0500]+)',f)
	roma = ''
	for r in rom:
		after = re.findall(u'([0-9][a-zA-Z]+)',r)
		for w in after:
			r  = r.replace(w ,w[1:]+w[0])
		roma = roma + r	+'\n'


	bar = re.findall(u'([\u0020\u002D][\u002D][\u002D]+[\u0020])',f)

	
	rom = re.findall(u'([\u0020-\u0500]+)',roma)#羅馬
	chi = re.findall(u'([\u0020\u4e00-\u9fff]+)',f)#漢字
	
	b = 0
	r = 0
	c = 0

	while r < len(rom) and c < len(chi) :
		if rom[r] == ' ':
			r += 1
			continue

		elif chi[c] == ' ':
			c += 1
			continue
		else:
			final.write(chi[c].replace(' ','',1)+'//'+rom[r].replace(' ','',1)+'\n')
			r += 1
			c += 1

	while r < len(rom):
		final.write(rom[r]+'\n')
		r += 1
	
	for q in chi:
		if q == ' ':
			continue
		o.write(q.replace(' ','',1)+'\n')
	for q in rom:
		if q == ' ':
			continue
		cc.write(q.replace(' ','',1)+'\n')	


	o.close()
	cc.close()
	print(n)
	'''
	print(rom)
	print(chi)
	print(bar)
	
	'''
	#\u000A 換行 \u0020 space




		

	'''
	a	á (U+00E1)	à (U+00E0)	ah	â (U+00E2)	ǎ (U+01CE)	ā (U+0101)	a̍h (U+0061 U+030D)	a̋ (U+0061 U+030B)
	e	é (U+00E9)	è (U+00E8)	eh	ê (U+00EA)	ě (U+011B)	ē (U+0113)	e̍h (U+0065 U+030D)	e̋ (U+0065 U+030B)
	i	í (U+00ED)	ì (U+00EC)	ih	î (U+00EE)	ǐ (U+01D0)	ī (U+012B)	i̍h (U+0069 U+030D)	i̋ (U+0069 U+030B)
	o	ó (U+00F3)	ò (U+00F2)	oh	ô (U+00F4)	ǒ (U+01D2)	ō (U+014D)	o̍h (U+006F U+030D)	ő (U+0151)
	u	ú (U+00FA)	ù (U+00F9)	uh	û (U+00FB)	ǔ (U+01D4)	ū (U+016B)	u̍h (U+0075 U+030D)	ű (U+0171)
	m	ḿ (U+1E3F)	m̀ (U+006D U+0300)	mh	m̂ (U+006D U+0302)	m̌ (U+006D U+030C)	m̄ (U+006D U+0304)	m̍h (U+006D U+030D)	m̋ (U+006D U+030B)
	n	ń (U+0144)	ǹ (U+01F9)	nh	n̂ (U+006E U+0302)	ň (U+0148)	n̄ (U+006E U+0304)	n̍h (U+006E U+030D)	n̋ (U+006E U+030B)
	'''