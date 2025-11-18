; Design a string manipulation tool which can do
; three different operation according to the user’s choice, 
; 1. Count the frequency of consonants in that string
; 2. Check if a substring exists in the main string
; 3. Remove vowels from the string
; 	You will have to use different procedures for each task.

; Steps:
;	1. Ask the user what he wants to do
;	2. Let him give a string until he presses ‘Enter.
;	3. Show outputs like,
;		- Frequency of the consonants in numbers (consider one digit)
;		- Or, show ‘Yes’ if the substring exists/’No’ if it doesn’t exist
;			(You have to take two inputs for this choice)
;		- Or, show the string without any vowels

.MODEL SMALL

; Macros here

PRINT_STRING MACRO STR
	LEA DX, STR
	MOV AH, 9
	INT 21h
ENDM

PRINT_CHAR MACRO X
	MOV DX, X
	MOV AH, 2
	INT 21H
ENDM    

NEWLCERT MACRO 
    PRINT_CHAR 0AH
    PRINT_CHAR 0DH
ENDM

CLR_SCRN MACRO
    MOV AX, 0600H
    MOV BH, 07H
    MOV CX, 0000H
    MOV DX, 184FH
    INT 10H

    MOV AH, 02H
    MOV BH, 00H
    MOV DH, 00H
    MOV DL, 00H
    INT 10H
ENDM

.STACK 100H
.DATA

p1 DB "STRING MANIPULATION:",0AH,0AH,0DH,"Choose Operation:",0AH,0AH,0DH,24H
p2 DB "1. Count frequency of consonants in a string.",0AH,0DH,24H
p3 DB "2. Check if a substring exists in the main string.",0AH,0DH,24H
p4 DB "3. Remove vowels from string",0AH,0AH,0DH,24H
p5 DB "(Enter mode 1, 2 or 3): $"
p6 DB "WRONG MODE INPUT !! Please Enter Again !",0DH,0AH,0AH,24H

MODE DB 0

p7 DB "Enter String: $"

STR_ARR   DB 100 DUP(?)
STR_LEN   DW 0
CAPvowels DB "AEIOU"
smlvowels DB "aeiou"

P11 DB "Consonant Frequency: $"
consCount DW 0

p210 DB "Enter Sub-string: $"
p211 DB "Sub-string Exists?: $"
p21y DB "Yes!$"
p21n DB "No!$"

SUB_ARR   DB 100 DUP(?)
SUB_LEN   DW 0

p31 DB "Vowels Removed!$"
p32 DB "New String: $"

NEW_STR   DB 100 DUP(?)
NEW_LEN   DW 0

.CODE

; Procedures here

STRING_INPUT PROC
    CLR_SCRN
    PRINT_STRING p7       
    MOV SI, 0
	L1:
    	MOV AH, 1
    	INT 21H
    	CMP AL, 0DH
    	JE	E1
    	MOV STR_ARR[SI], AL
    	INC SI
    	ADD STR_LEN, 1
    	JMP L1
    E1:
    NEWLCERT
STRING_INPUT ENDP
JMP EX_IN 

ConsFreq PROC
    MOV SI, 0
    MOV CX, STR_LEN
    L10:
        MOV AL, STR_ARR[SI]
        CMP AL, 41H
        JL  C10
        CMP AL, 5AH
        JG  SMALL1
        JMP CAP_VOWEL_CHECK1
               
        SMALL1:
        CMP AL, 61H
        JL  C10
        CMP AL, 7AH
        JG  C10
        JMP SML_VOWEL_CHECK1
        
        CAP_VOWEL_CHECK1:
        MOV DI, 0
        L11:
            MOV BL, CAPvowels[DI]
            CMP AL, BL
            JE  C10
            INC DI
            CMP DI, 5
            JE  C11
            JMP L11    
        C11:
        ADD consCount, 1
        JMP C10
        
        SML_VOWEL_CHECK1:
        MOV DI, 0
        L12:
            MOV BL, smlvowels[DI]
            CMP AL, BL
            JE  C10
            INC DI
            CMP DI, 5
            JE  C12
            JMP L12    
        C12:
        ADD consCount, 1
        
        C10:
        INC SI
    LOOP L10
    
    MOV AX, consCount
	MOV BX, 10
	MOV CX, 0
	ASCII_CONVERT:
		MOV DX, 0
		DIV BX
		ADD DX, 30H
		PUSH DX
		INC CX
		CMP AX, 0
		JE	PRINT
		JMP ASCII_CONVERT
	PRINT:
		POP DX
		PRINT_CHAR DX
	LOOP PRINT
ConsFreq ENDP
JMP EX

Substring PROC
    PRINT_STRING p210       
    MOV SI, 0
	L20:
    	MOV AH, 1
    	INT 21H
    	CMP AL, 0DH
    	JE	E20
    	MOV SUB_ARR[SI], AL
    	INC SI
    	ADD SUB_LEN, 1
    	JMP L20
    E20:
    NEWLCERT
    PRINT_STRING p211
    
    MOV CX, STR_LEN
    MOV BX, SUB_LEN
    CMP CX, BX
    JL  NOT_EXIST
    
    
    SUB CX, BX
    INC CX
    MOV BX, 0
    MOV DX, SUB_LEN
    L21:
        MOV SI, 0
        L211:
            MOV AL, STR_ARR[BX+SI]
            MOV AH, SUB_ARR[SI]
            CMP AL, AH
            JE  C211
            JMP C21
            C211:
            INC SI
            CMP SI, DX
            JE  MATCH_FOUND
            JMP L211
        C21:
        INC BX
    LOOP L21
    
    NOT_EXIST:
    PRINT_STRING p21n
    JMP E2
    
    MATCH_FOUND:
    PRINT_STRING p21y
    E2:
    
Substring ENDP
JMP EX

RemoveVowels PROC
    PRINT_STRING p31
    NEWLCERT
    PRINT_STRING p32
    
    MOV SI, 0
    MOV DI, 0
    MOV CX, STR_LEN
    L30:
        MOV AL, STR_ARR[SI]
        CMP AL, 41H
        JL  NOTLETTER2
        CMP AL, 5AH
        JG  SMALL2
        JMP CAP_VOWEL_CHECK2
               
        SMALL2:
        CMP AL, 61H
        JL  NOTLETTER2
        CMP AL, 7AH
        JG  NOTLETTER2
        JMP SML_VOWEL_CHECK2
        
        CAP_VOWEL_CHECK2:
        PUSH DI
        MOV DI, 0
        L31:
            MOV BL, CAPvowels[DI]
            CMP AL, BL
            JE  E30
            INC DI
            CMP DI, 5
            JE  NOTVOW2
            JMP L31
        
        SML_VOWEL_CHECK2:
        PUSH DI
        MOV DI, 0
        L32:
            MOV BL, smlvowels[DI]
            CMP AL, BL
            JE  E30
            INC DI
            CMP DI, 5
            JE  NOTVOW2
            JMP L32    
        
        NOTVOW2:
        POP DI
        MOV NEW_STR[DI], AL
        PRINT_CHAR AX
        INC DI
        JMP E30
        
        NOTLETTER2:
        MOV NEW_STR[DI], AL
        PRINT_CHAR AX
        INC DI
        
        E30:
        INC SI
    LOOP L30   
    
RemoveVowels ENDP
JMP EX

MAIN PROC

; initialize DS
MOV AX,@DATA
MOV DS,AX
 
; code here

    C0:
    PRINT_STRING p1
    PRINT_STRING p2
    PRINT_STRING p3
    PRINT_STRING p4
    PRINT_STRING p5

    MOV AH, 1
    INT 21H
    
    MOV MODE, AL
    CMP AL, 31H
    JL  CE
    CMP AL, 33H
    JG  CE
    CALL STRING_INPUT
    
    EX_IN:
    MOV AL, MODE
    CMP AL, 31H
    JNE MODE2
    CALL ConsFreq
    MODE2:
    CMP AL, 32H
    JNE MODE3
    CALL Substring
    MODE3:
    CALL RemoveVowels
    
    CE:
    CLR_SCRN
    PRINT_STRING p6
    JMP C0

    EX:

;exit to DOS			  
MOV AX, 4C00H
INT 21H

MAIN ENDP
    END MAIN

