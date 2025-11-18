.MODEL SMALL
 
.STACK 100H

.DATA

; declare variables here
A DB " is greater!$"
B DB "Please insert INPUT A: $"
C DB "Please insert INPUT B: $"
                  
.CODE
MAIN PROC

; initialize DS

MOV AX,@DATA
MOV DS,AX
 
; enter your code here    

; INPUT 1
LEA DX,B
mov AH,9
int 21h

mov AH,1
int 21h

MOV BH, AL

; newline
MOV AH,2 
MOV DL,0DH 
INT 21H
MOV DL,0AH 
INT 21h

; INPUT 2
LEA DX,C
mov AH,9
int 21h

mov AH,1
int 21h

MOV CH, AL

; newline
MOV AH,2 
MOV DL,0DH 
INT 21H
MOV DL,0AH 
INT 21h 

; CONDITIONS:
CMP BH, CH
JL ELSE_BLOCK

MOV DL, BH
MOV AH, 2
INT 21h

JMP EXIT               

ELSE_BLOCK:
MOV DL, CH
MOV AH, 2
INT 21h

; OUTPUT
EXIT:
LEA DX,A
mov AH,9
int 21h
;exit to DOS
               
MOV AX, 4C00H
INT 21H

MAIN ENDP
	END MAIN
