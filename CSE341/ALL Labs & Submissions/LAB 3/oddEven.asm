.MODEL SMALL
 
.STACK 100H

.DATA

; declare variables here
A DB "INPUT Between 1 to 4: $"
                  
.CODE
MAIN PROC

; initialize DS

MOV AX,@DATA
MOV DS,AX
 
; enter your code here    

; INPUT
LEA DX,A
mov AH,9
int 21h

mov AH,1
int 21h

MOV BH, AL
SUB BH, 30H

; newline
MOV AH,2 
MOV DL,0DH 
INT 21H
MOV DL,0AH 
INT 21h 

; CONDITIONS:
CMP BH, 1
JE PRINT_O
CMP BH, 2
JE PRINT_E
CMP BH, 3
JE PRINT_O
CMP BH, 4
JE PRINT_E

;PRINT 0DD
PRINT_O:
MOV DL, 4FH
MOV AH, 2
INT 21h

JMP EXIT               

;PRINT EVEN
PRINT_E:
MOV DL, 45H
MOV AH, 2
INT 21h

; OUTPUT
EXIT:
;exit to DOS
               
MOV AX, 4C00H
INT 21H

MAIN ENDP
	END MAIN
