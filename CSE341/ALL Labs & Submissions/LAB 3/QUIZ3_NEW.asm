.MODEL SMALL
 
.STACK 100H

.DATA

; declare variables here
A DB "Enter the first side: $"
B DB "Enter the second side: $"
C DB "Enter the third side: $"
D DB "This is an Equilateral Triangle.$"
E DB "This is an Isosceles Triangle.$"
F DB "This is a Scalene Triangle.$"
G DB "This is an invalid Triangle.$"
                  
.CODE
MAIN PROC

; initialize DS

MOV AX,@DATA
MOV DS,AX
 
; enter your code here    

; INPUTS
LEA DX,A
mov AH,9
int 21h

mov AH,1
int 21h
SUB AL, 30h
MOV DL, 10
MUL DL

MOV BL, AL

mov AH,1
int 21h    

ADD BL, AL
SUB BL, 30h

; newline
MOV AH,2 
MOV DL,0DH 
INT 21H
MOV DL,0AH 
INT 21h

LEA DX,B
mov AH,9
int 21h

mov AH,1
int 21h
SUB AL, 30h
MOV DL, 10
MUL DL

MOV BH, AL

mov AH,1
int 21h    

ADD BH, AL
SUB BH, 30h

; newline
MOV AH,2 
MOV DL,0DH 
INT 21H
MOV DL,0AH 
INT 21h

LEA DX,C
mov AH,9
int 21h

mov AH,1
int 21h
SUB AL, 30h
MOV DL, 10
MUL DL

MOV CL, AL

mov AH,1
int 21h    

ADD CL, AL
SUB CL, 30h

; newline
MOV AH,2 
MOV DL,0DH 
INT 21H
MOV DL,0AH 
INT 21h

; CONDITIONS:
MOV DH, 0
ADD DH, BL
ADD DH, BH
CMP DH, CL
JLE INVALID

MOV DH, 0
ADD DH, BH
ADD DH, CL
CMP DH, BL
JLE INVALID
          
MOV DH, 0
ADD DH, BL
ADD DH, CL
CMP DH, BH
JLE INVALID

CMP BL, BH
JE TWOEQUAL
CMP BH, CL 
JE TWOEQUAL
CMP BL, CL 
JE TWOEQUAL

LEA DX,F
mov AH,9
int 21h
JMP EXIT

TWOEQUAL:
CMP BH, CL
JE ALLEQUAL
LEA DX,E
mov AH,9
int 21h
JMP EXIT


ALLEQUAL:
LEA DX,D
mov AH,9
int 21h
JMP EXIT
          
          
INVALID:
LEA DX,G
mov AH,9
int 21h

; OUTPUT
EXIT:

;exit to DOS

MAIN ENDP
	END MAIN
