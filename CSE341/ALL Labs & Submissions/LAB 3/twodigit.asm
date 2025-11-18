.MODEL SMALL
 
.STACK 100H

.DATA

; declare variables here
A DB "Please insert INPUT 1: $"
B DB "Please insert INPUT 2: $"
R DB "Result: $"
                  
.CODE
MAIN PROC

; initialize DS

MOV AX,@DATA
MOV DS,AX
 
; enter your code here    

; INPUT 1
LEA DX,A
mov AH,9
int 21h

mov AH,1
int 21h

MOV CL, AL
SUB CL, 30H

MOV AH,2 
MOV DL,0DH 
INT 21H
MOV DL,0AH 
INT 21h

; INPUT 2 AND ADD
LEA DX,B
mov AH,9
int 21h

mov AH,1
int 21h

ADD AL, CL
SUB AL, 30H

; Handling for 2 digits
MOV AH, 0
MOV DL, 10
DIV DL
MOV CX, AX

; newline
MOV AH,2 
MOV DL,0DH 
INT 21H
MOV DL,0AH 
INT 21h 
 
; VIEW RESULT: 
LEA DX,R
mov AH,9
int 21h               
         
MOV DL, CL
ADD DL, 30H
MOV AH, 2
INT 21h

MOV DL, CH
ADD DL, 30H
MOV AH, 2
INT 21h

;exit to DOS
               
MOV AX, 4C00H
INT 21H

MAIN ENDP
	END MAIN
