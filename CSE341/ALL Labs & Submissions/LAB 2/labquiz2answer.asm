.MODEL SMALL
 
.STACK 100H

.DATA

; declare variables here
A DB "Please insert digit 1: $"
B DB "Please insert digit 2: $"
R DB "The final answer is: $"
                  
.CODE
MAIN PROC

; initialize DS

MOV AX,@DATA
MOV DS,AX
 
; enter your code here    

; digit 1
LEA DX,A
mov AH,9
int 21h

mov AH,1
int 21h

MOV CL, AL
SUB CL, 30H

;newline
MOV AH,2 
MOV DL,0DH 
INT 21H
MOV DL,0AH 
INT 21h

; digit 2
LEA DX,B
mov AH,9
int 21h

mov AH,1
int 21h

MOV CH, AL
SUB CH, 30H

; newline
MOV AH,2 
MOV DL,0DH 
INT 21H
MOV DL,0AH 
INT 21h 
 
; MATH: 
MOV AL, 50
MUL CL

MOV CL, CH
MOV CH, 0

ADD AX, CX
ADD AX, 50

MOV BX, AX

; PRINT RESULT
LEA DX,R
mov AH,9
int 21h               

MOV AX, BX
MOV BL, 100
DIV BL

MOV BH, AH

MOV DL, AL
ADD DL, 30H
MOV AH, 2
INT 21h         

MOV AL, BH
MOV AH, 0
MOV BX, 10
DIV BL

MOV BL, AH

MOV DL, AL
ADD DL, 30H
MOV AH, 2
INT 21h         

MOV DL, BL
MOV AH, 2
ADD DL, 30H
INT 21h         


;exit to DOS
               
MOV AX, 4C00H
INT 21H

MAIN ENDP
END MAIN