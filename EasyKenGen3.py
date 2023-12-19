from sympy import symbols, Eq, solve

input_text = """
dword_40D000    dd 0                    
.data:0040D004                 db  96h
.data:0040D005                 db  30h ; 0
.data:0040D006                 db    7
.data:0040D007                 db  77h ; w
.data:0040D008                 db  2Ch ; ,
.data:0040D009                 db  61h ; a
.data:0040D00A                 db  0Eh
.data:0040D00B                 db 0EEh
.data:0040D00C                 db 0BAh
.data:0040D00D                 db  51h ; Q
.data:0040D00E                 db    9
.data:0040D00F                 db  99h
.data:0040D010                 db  19h
.data:0040D011                 db 0C4h
.data:0040D012                 db  6Dh ; m
.data:0040D013                 db    7
.data:0040D014                 db  8Fh
.data:0040D015                 db 0F4h
.data:0040D016                 db  6Ah ; j
.data:0040D017                 db  70h ; p
.data:0040D018                 db  35h ; 5
.data:0040D019                 db 0A5h
.data:0040D01A                 db  63h ; c
.data:0040D01B                 db 0E9h
.data:0040D01C                 db 0A3h
.data:0040D01D                 db  95h
.data:0040D01E                 db  64h ; d
.data:0040D01F                 db  9Eh
.data:0040D020                 db  32h ; 2
.data:0040D021                 db  88h
.data:0040D022                 db 0DBh
.data:0040D023                 db  0Eh
.data:0040D024                 db 0A4h
.data:0040D025                 db 0B8h
.data:0040D026                 db 0DCh
.data:0040D027                 db  79h ; y
.data:0040D028                 db  1Eh
.data:0040D029                 db 0E9h
.data:0040D02A                 db 0D5h
.data:0040D02B                 db 0E0h
.data:0040D02C                 db  88h
.data:0040D02D                 db 0D9h
.data:0040D02E                 db 0D2h
.data:0040D02F                 db  97h
.data:0040D030                 db  2Bh ; +
.data:0040D031                 db  4Ch ; L
.data:0040D032                 db 0B6h
.data:0040D033                 db    9
.data:0040D034                 db 0BDh
.data:0040D035                 db  7Ch ; |
.data:0040D036                 db 0B1h
.data:0040D037                 db  7Eh ; ~
.data:0040D038                 db    7
.data:0040D039                 db  2Dh ; -
.data:0040D03A                 db 0B8h
.data:0040D03B                 db 0E7h
.data:0040D03C                 db  91h
.data:0040D03D                 db  1Dh
.data:0040D03E                 db 0BFh
.data:0040D03F                 db  90h
.data:0040D040                 db  64h ; d
.data:0040D041                 db  10h
.data:0040D042                 db 0B7h
.data:0040D043                 db  1Dh
.data:0040D044                 db 0F2h
.data:0040D045                 db  20h
.data:0040D046                 db 0B0h
.data:0040D047                 db  6Ah ; j
.data:0040D048                 db  48h ; H
.data:0040D049                 db  71h ; q
.data:0040D04A                 db 0B9h
.data:0040D04B                 db 0F3h
.data:0040D04C                 db 0DEh
.data:0040D04D                 db  41h ; A
.data:0040D04E                 db 0BEh
.data:0040D04F                 db  84h
.data:0040D050                 db  7Dh ; }
.data:0040D051                 db 0D4h
.data:0040D052                 db 0DAh
.data:0040D053                 db  1Ah
.data:0040D054                 db 0EBh
.data:0040D055                 db 0E4h
.data:0040D056                 db 0DDh
.data:0040D057                 db  6Dh ; m
.data:0040D058                 db  51h ; Q
.data:0040D059                 db 0B5h
.data:0040D05A                 db 0D4h
.data:0040D05B                 db 0F4h
.data:0040D05C                 db 0C7h
.data:0040D05D                 db  85h
.data:0040D05E                 db 0D3h
.data:0040D05F                 db  83h
.data:0040D060                 db  56h ; V
.data:0040D061                 db  98h
.data:0040D062                 db  6Ch ; l
.data:0040D063                 db  13h
.data:0040D064                 db 0C0h
.data:0040D065                 db 0A8h
.data:0040D066                 db  6Bh ; k
.data:0040D067                 db  64h ; d
.data:0040D068                 db  7Ah ; z
.data:0040D069                 db 0F9h
.data:0040D06A                 db  62h ; b
.data:0040D06B                 db 0FDh
.data:0040D06C                 db 0ECh
.data:0040D06D                 db 0C9h
.data:0040D06E                 db  65h ; e
.data:0040D06F                 db  8Ah
.data:0040D070                 db  4Fh ; O
.data:0040D071                 db  5Ch ; 
.data:0040D072                 db    1
.data:0040D073                 db  14h
.data:0040D074                 db 0D9h
.data:0040D075                 db  6Ch ; l
.data:0040D076                 db    6
.data:0040D077                 db  63h ; c
.data:0040D078                 db  63h ; c
.data:0040D079                 db  3Dh ; =
.data:0040D07A                 db  0Fh
.data:0040D07B                 db 0FAh
.data:0040D07C                 db 0F5h
.data:0040D07D                 db  0Dh
.data:0040D07E                 db    8
.data:0040D07F                 db  8Dh
.data:0040D080                 db 0C8h
.data:0040D081                 db  20h
.data:0040D082                 db  6Eh ; n
.data:0040D083                 db  3Bh ; ;
.data:0040D084                 db  5Eh ; ^
.data:0040D085                 db  10h
.data:0040D086                 db  69h ; i
.data:0040D087                 db  4Ch ; L
.data:0040D088                 db 0E4h
.data:0040D089                 db  41h ; A
.data:0040D08A                 db  60h ; `
.data:0040D08B                 db 0D5h
.data:0040D08C                 db  72h ; r
.data:0040D08D                 db  71h ; q
.data:0040D08E                 db  67h ; g
.data:0040D08F                 db 0A2h
.data:0040D090                 db 0D1h
.data:0040D091                 db 0E4h
.data:0040D092                 db    3
.data:0040D093                 db  3Ch ; <
.data:0040D094                 db  47h ; G
.data:0040D095                 db 0D4h
.data:0040D096                 db    4
.data:0040D097                 db  4Bh ; K
.data:0040D098                 db 0FDh
.data:0040D099                 db  85h
.data:0040D09A                 db  0Dh
.data:0040D09B                 db 0D2h
.data:0040D09C                 db  6Bh ; k
.data:0040D09D                 db 0B5h
.data:0040D09E                 db  0Ah
.data:0040D09F                 db 0A5h
.data:0040D0A0                 db 0FAh
.data:0040D0A1                 db 0A8h
.data:0040D0A2                 db 0B5h
.data:0040D0A3                 db  35h ; 5
.data:0040D0A4                 db  6Ch ; l
.data:0040D0A5                 db  98h
.data:0040D0A6                 db 0B2h
.data:0040D0A7                 db  42h ; B
.data:0040D0A8                 db 0D6h
.data:0040D0A9                 db 0C9h
.data:0040D0AA                 db 0BBh
.data:0040D0AB                 db 0DBh
.data:0040D0AC                 db  40h ; @
.data:0040D0AD                 db 0F9h
.data:0040D0AE                 db 0BCh
.data:0040D0AF                 db 0ACh
.data:0040D0B0                 db 0E3h
.data:0040D0B1                 db  6Ch ; l
.data:0040D0B2                 db 0D8h
.data:0040D0B3                 db  32h ; 2
.data:0040D0B4                 db  75h ; u
.data:0040D0B5                 db  5Ch ; 
.data:0040D0B6                 db 0DFh
.data:0040D0B7                 db  45h ; E
.data:0040D0B8                 db 0CFh
.data:0040D0B9                 db  0Dh
.data:0040D0BA                 db 0D6h
.data:0040D0BB                 db 0DCh
.data:0040D0BC                 db  59h ; Y
.data:0040D0BD                 db  3Dh ; =
.data:0040D0BE                 db 0D1h
.data:0040D0BF                 db 0ABh
.data:0040D0C0                 db 0ACh
.data:0040D0C1                 db  30h ; 0
.data:0040D0C2                 db 0D9h
.data:0040D0C3                 db  26h ; &
.data:0040D0C4                 db  3Ah ; :
.data:0040D0C5                 db    0
.data:0040D0C6                 db 0DEh
.data:0040D0C7                 db  51h ; Q
.data:0040D0C8                 db  80h
.data:0040D0C9                 db  51h ; Q
.data:0040D0CA                 db 0D7h
.data:0040D0CB                 db 0C8h
.data:0040D0CC                 db  16h
.data:0040D0CD                 db  61h ; a
.data:0040D0CE                 db 0D0h
.data:0040D0CF                 db 0BFh
.data:0040D0D0                 db 0B5h
.data:0040D0D1                 db 0F4h
.data:0040D0D2                 db 0B4h
.data:0040D0D3                 db  21h ; !
.data:0040D0D4                 db  23h ; #
.data:0040D0D5                 db 0C4h
.data:0040D0D6                 db 0B3h
.data:0040D0D7                 db  56h ; V
.data:0040D0D8                 db  99h
.data:0040D0D9                 db  95h
.data:0040D0DA                 db 0BAh
.data:0040D0DB                 db 0CFh
.data:0040D0DC                 db  0Fh
.data:0040D0DD                 db 0A5h
.data:0040D0DE                 db 0BDh
.data:0040D0DF                 db 0B8h
.data:0040D0E0                 db  9Eh
.data:0040D0E1                 db 0B8h
.data:0040D0E2                 db    2
.data:0040D0E3                 db  28h ; (
.data:0040D0E4                 db    8
.data:0040D0E5                 db  88h
.data:0040D0E6                 db    5
.data:0040D0E7                 db  5Fh ; _
.data:0040D0E8                 db 0B2h
.data:0040D0E9                 db 0D9h
.data:0040D0EA                 db  0Ch
.data:0040D0EB                 db 0C6h
.data:0040D0EC                 db  24h ; $
.data:0040D0ED                 db 0E9h
.data:0040D0EE                 db  0Bh
.data:0040D0EF                 db 0B1h
.data:0040D0F0                 db  87h
.data:0040D0F1                 db  7Ch ; |
.data:0040D0F2                 db  6Fh ; o
.data:0040D0F3                 db  2Fh ; /
.data:0040D0F4                 db  11h
.data:0040D0F5                 db  4Ch ; L
.data:0040D0F6                 db  68h ; h
.data:0040D0F7                 db  58h ; X
.data:0040D0F8                 db 0ABh
.data:0040D0F9                 db  1Dh
.data:0040D0FA                 db  61h ; a
.data:0040D0FB                 db 0C1h
.data:0040D0FC                 db  3Dh ; =
.data:0040D0FD                 db  2Dh ; -
.data:0040D0FE                 db  66h ; f
.data:0040D0FF                 db 0B6h
.data:0040D100                 db  90h
.data:0040D101                 db  41h ; A
.data:0040D102                 db 0DCh
.data:0040D103                 db  76h ; v
.data:0040D104                 db    6
.data:0040D105                 db  71h ; q
.data:0040D106                 db 0DBh
.data:0040D107                 db    1
.data:0040D108                 db 0BCh
.data:0040D109                 db  20h
.data:0040D10A                 db 0D2h
.data:0040D10B                 db  98h
.data:0040D10C                 db  2Ah ; *
.data:0040D10D                 db  10h
.data:0040D10E                 db 0D5h
.data:0040D10F                 db 0EFh
.data:0040D110                 db  89h
.data:0040D111                 db  85h
.data:0040D112                 db 0B1h
.data:0040D113                 db  71h ; q
.data:0040D114                 db  1Fh
.data:0040D115                 db 0B5h
.data:0040D116                 db 0B6h
.data:0040D117                 db    6
.data:0040D118                 db 0A5h
.data:0040D119                 db 0E4h
.data:0040D11A                 db 0BFh
.data:0040D11B                 db  9Fh
.data:0040D11C                 db  33h ; 3
.data:0040D11D                 db 0D4h
.data:0040D11E                 db 0B8h
.data:0040D11F                 db 0E8h
.data:0040D120                 db 0A2h
.data:0040D121                 db 0C9h
.data:0040D122                 db    7
.data:0040D123                 db  78h ; x
.data:0040D124                 db  34h ; 4
.data:0040D125                 db 0F9h
.data:0040D126                 db    0
.data:0040D127                 db  0Fh
.data:0040D128                 db  8Eh
.data:0040D129                 db 0A8h
.data:0040D12A                 db    9
.data:0040D12B                 db  96h
.data:0040D12C                 db  18h
.data:0040D12D                 db  98h
.data:0040D12E                 db  0Eh
.data:0040D12F                 db 0E1h
.data:0040D130                 db 0BBh
.data:0040D131                 db  0Dh
.data:0040D132                 db  6Ah ; j
.data:0040D133                 db  7Fh ; 
.data:0040D134                 db  2Dh ; -
.data:0040D135                 db  3Dh ; =
.data:0040D136                 db  6Dh ; m
.data:0040D137                 db    8
.data:0040D138                 db  97h
.data:0040D139                 db  6Ch ; l
.data:0040D13A                 db  64h ; d
.data:0040D13B                 db  91h
.data:0040D13C                 db    1
.data:0040D13D                 db  5Ch ; 
.data:0040D13E                 db  63h ; c
.data:0040D13F                 db 0E6h
.data:0040D140                 db 0F4h
.data:0040D141                 db  51h ; Q
.data:0040D142                 db  6Bh ; k
.data:0040D143                 db  6Bh ; k
.data:0040D144                 db  62h ; b
.data:0040D145                 db  61h ; a
.data:0040D146                 db  6Ch ; l
.data:0040D147                 db  1Ch
.data:0040D148                 db 0D8h
.data:0040D149                 db  30h ; 0
.data:0040D14A                 db  65h ; e
.data:0040D14B                 db  85h
.data:0040D14C                 db  4Eh ; N
.data:0040D14D                 db    0
.data:0040D14E                 db  62h ; b
.data:0040D14F                 db 0F2h
.data:0040D150                 db 0EDh
.data:0040D151                 db  95h
.data:0040D152                 db    6
.data:0040D153                 db  6Ch ; l
.data:0040D154                 db  7Bh ; {
.data:0040D155                 db 0A5h
.data:0040D156                 db    1
.data:0040D157                 db  1Bh
.data:0040D158                 db 0C1h
.data:0040D159                 db 0F4h
.data:0040D15A                 db    8
.data:0040D15B                 db  82h
.data:0040D15C                 db  57h ; W
.data:0040D15D                 db 0C4h
.data:0040D15E                 db  0Fh
.data:0040D15F                 db 0F5h
.data:0040D160                 db 0C6h
.data:0040D161                 db 0D9h
.data:0040D162                 db 0B0h
.data:0040D163                 db  65h ; e
.data:0040D164                 db  50h ; P
.data:0040D165                 db 0E9h
.data:0040D166                 db 0B7h
.data:0040D167                 db  12h
.data:0040D168                 db 0EAh
.data:0040D169                 db 0B8h
.data:0040D16A                 db 0BEh
.data:0040D16B                 db  8Bh
.data:0040D16C                 db  7Ch ; |
.data:0040D16D                 db  88h
.data:0040D16E                 db 0B9h
.data:0040D16F                 db 0FCh
.data:0040D170                 db 0DFh
.data:0040D171                 db  1Dh
.data:0040D172                 db 0DDh
.data:0040D173                 db  62h ; b
.data:0040D174                 db  49h ; I
.data:0040D175                 db  2Dh ; -
.data:0040D176                 db 0DAh
.data:0040D177                 db  15h
.data:0040D178                 db 0F3h
.data:0040D179                 db  7Ch ; |
.data:0040D17A                 db 0D3h
.data:0040D17B                 db  8Ch
.data:0040D17C                 db  65h ; e
.data:0040D17D                 db  4Ch ; L
.data:0040D17E                 db 0D4h
.data:0040D17F                 db 0FBh
.data:0040D180                 db  58h ; X
.data:0040D181                 db  61h ; a
.data:0040D182                 db 0B2h
.data:0040D183                 db  4Dh ; M
.data:0040D184                 db 0CEh
.data:0040D185                 db  51h ; Q
.data:0040D186                 db 0B5h
.data:0040D187                 db  3Ah ; :
.data:0040D188                 db  74h ; t
.data:0040D189                 db    0
.data:0040D18A                 db 0BCh
.data:0040D18B                 db 0A3h
.data:0040D18C                 db 0E2h
.data:0040D18D                 db  30h ; 0
.data:0040D18E                 db 0BBh
.data:0040D18F                 db 0D4h
.data:0040D190                 db  41h ; A
.data:0040D191                 db 0A5h
.data:0040D192                 db 0DFh
.data:0040D193                 db  4Ah ; J
.data:0040D194                 db 0D7h
.data:0040D195                 db  95h
.data:0040D196                 db 0D8h
.data:0040D197                 db  3Dh ; =
.data:0040D198                 db  6Dh ; m
.data:0040D199                 db 0C4h
.data:0040D19A                 db 0D1h
.data:0040D19B                 db 0A4h
.data:0040D19C                 db 0FBh
.data:0040D19D                 db 0F4h
.data:0040D19E                 db 0D6h
.data:0040D19F                 db 0D3h
.data:0040D1A0                 db  6Ah ; j
.data:0040D1A1                 db 0E9h
.data:0040D1A2                 db  69h ; i
.data:0040D1A3                 db  43h ; C
.data:0040D1A4                 db 0FCh
.data:0040D1A5                 db 0D9h
.data:0040D1A6                 db  6Eh ; n
.data:0040D1A7                 db  34h ; 4
.data:0040D1A8                 db  46h ; F
.data:0040D1A9                 db  88h
.data:0040D1AA                 db  67h ; g
.data:0040D1AB                 db 0ADh
.data:0040D1AC                 db 0D0h
.data:0040D1AD                 db 0B8h
.data:0040D1AE                 db  60h ; `
.data:0040D1AF                 db 0DAh
.data:0040D1B0                 db  73h ; s
.data:0040D1B1                 db  2Dh ; -
.data:0040D1B2                 db    4
.data:0040D1B3                 db  44h ; D
.data:0040D1B4                 db 0E5h
.data:0040D1B5                 db  1Dh
.data:0040D1B6                 db    3
.data:0040D1B7                 db  33h ; 3
.data:0040D1B8                 db  5Fh ; _
.data:0040D1B9                 db  4Ch ; L
.data:0040D1BA                 db  0Ah
.data:0040D1BB                 db 0AAh
.data:0040D1BC                 db 0C9h
.data:0040D1BD                 db  7Ch ; |
.data:0040D1BE                 db  0Dh
.data:0040D1BF                 db 0DDh
.data:0040D1C0                 db  3Ch ; <
.data:0040D1C1                 db  71h ; q
.data:0040D1C2                 db    5
.data:0040D1C3                 db  50h ; P
.data:0040D1C4                 db 0AAh
.data:0040D1C5                 db  41h ; A
.data:0040D1C6                 db    2
.data:0040D1C7                 db  27h ; '
.data:0040D1C8                 db  10h
.data:0040D1C9                 db  10h
.data:0040D1CA                 db  0Bh
.data:0040D1CB                 db 0BEh
.data:0040D1CC                 db  86h
.data:0040D1CD                 db  20h
.data:0040D1CE                 db  0Ch
.data:0040D1CF                 db 0C9h
.data:0040D1D0                 db  25h ; %
.data:0040D1D1                 db 0B5h
.data:0040D1D2                 db  68h ; h
.data:0040D1D3                 db  57h ; W
.data:0040D1D4                 db 0B3h
.data:0040D1D5                 db  85h
.data:0040D1D6                 db  6Fh ; o
.data:0040D1D7                 db  20h
.data:0040D1D8                 db    9
.data:0040D1D9                 db 0D4h
.data:0040D1DA                 db  66h ; f
.data:0040D1DB                 db 0B9h
.data:0040D1DC                 db  9Fh
.data:0040D1DD                 db 0E4h
.data:0040D1DE                 db  61h ; a
.data:0040D1DF                 db 0CEh
.data:0040D1E0                 db  0Eh
.data:0040D1E1                 db 0F9h
.data:0040D1E2                 db 0DEh
.data:0040D1E3                 db  5Eh ; ^
.data:0040D1E4                 db  98h
.data:0040D1E5                 db 0C9h
.data:0040D1E6                 db 0D9h
.data:0040D1E7                 db  29h ; )
.data:0040D1E8                 db  22h ; "
.data:0040D1E9                 db  98h
.data:0040D1EA                 db 0D0h
.data:0040D1EB                 db 0B0h
.data:0040D1EC                 db 0B4h
.data:0040D1ED                 db 0A8h
.data:0040D1EE                 db 0D7h
.data:0040D1EF                 db 0C7h
.data:0040D1F0                 db  17h
.data:0040D1F1                 db  3Dh ; =
.data:0040D1F2                 db 0B3h
.data:0040D1F3                 db  59h ; Y
.data:0040D1F4                 db  81h
.data:0040D1F5                 db  0Dh
.data:0040D1F6                 db 0B4h
.data:0040D1F7                 db  2Eh ; .
.data:0040D1F8                 db  3Bh ; ;
.data:0040D1F9                 db  5Ch ; 
.data:0040D1FA                 db 0BDh
.data:0040D1FB                 db 0B7h
.data:0040D1FC                 db 0ADh
.data:0040D1FD                 db  6Ch ; l
.data:0040D1FE                 db 0BAh
.data:0040D1FF                 db 0C0h
.data:0040D200                 db  20h
.data:0040D201                 db  83h
.data:0040D202                 db 0B8h
.data:0040D203                 db 0EDh
.data:0040D204                 db 0B6h
.data:0040D205                 db 0B3h
.data:0040D206                 db 0BFh
.data:0040D207                 db  9Ah
.data:0040D208                 db  0Ch
.data:0040D209                 db 0E2h
.data:0040D20A                 db 0B6h
.data:0040D20B                 db    3
.data:0040D20C                 db  9Ah
.data:0040D20D                 db 0D2h
.data:0040D20E                 db 0B1h
.data:0040D20F                 db  74h ; t
.data:0040D210                 db  39h ; 9
.data:0040D211                 db  47h ; G
.data:0040D212                 db 0D5h
.data:0040D213                 db 0EAh
.data:0040D214                 db 0AFh
.data:0040D215                 db  77h ; w
.data:0040D216                 db 0D2h
.data:0040D217                 db  9Dh
.data:0040D218                 db  15h
.data:0040D219                 db  26h ; &
.data:0040D21A                 db 0DBh
.data:0040D21B                 db    4
.data:0040D21C                 db  83h
.data:0040D21D                 db  16h
.data:0040D21E                 db 0DCh
.data:0040D21F                 db  73h ; s
.data:0040D220                 db  12h
.data:0040D221                 db  0Bh
.data:0040D222                 db  63h ; c
.data:0040D223                 db 0E3h
.data:0040D224                 db  84h
.data:0040D225                 db  3Bh ; ;
.data:0040D226                 db  64h ; d
.data:0040D227                 db  94h
.data:0040D228                 db  3Eh ; >
.data:0040D229                 db  6Ah ; j
.data:0040D22A                 db  6Dh ; m
.data:0040D22B                 db  0Dh
.data:0040D22C                 db 0A8h
.data:0040D22D                 db  5Ah ; Z
.data:0040D22E                 db  6Ah ; j
.data:0040D22F                 db  7Ah ; z
.data:0040D230                 db  0Bh
.data:0040D231                 db 0CFh
.data:0040D232                 db  0Eh
.data:0040D233                 db 0E4h
.data:0040D234                 db  9Dh
.data:0040D235                 db 0FFh
.data:0040D236                 db    9
.data:0040D237                 db  93h
.data:0040D238                 db  27h ; '
.data:0040D239                 db 0AEh
.data:0040D23A                 db    0
.data:0040D23B                 db  0Ah
.data:0040D23C                 db 0B1h
.data:0040D23D                 db  9Eh
.data:0040D23E                 db    7
.data:0040D23F                 db  7Dh ; }
.data:0040D240                 db  44h ; D
.data:0040D241                 db  93h
.data:0040D242                 db  0Fh
.data:0040D243                 db 0F0h
.data:0040D244                 db 0D2h
.data:0040D245                 db 0A3h
.data:0040D246                 db    8
.data:0040D247                 db  87h
.data:0040D248                 db  68h ; h
.data:0040D249                 db 0F2h
.data:0040D24A                 db    1
.data:0040D24B                 db  1Eh
.data:0040D24C                 db 0FEh
.data:0040D24D                 db 0C2h
.data:0040D24E                 db    6
.data:0040D24F                 db  69h ; i
.data:0040D250                 db  5Dh ; ]
.data:0040D251                 db  57h ; W
.data:0040D252                 db  62h ; b
.data:0040D253                 db 0F7h
.data:0040D254                 db 0CBh
.data:0040D255                 db  67h ; g
.data:0040D256                 db  65h ; e
.data:0040D257                 db  80h
.data:0040D258                 db  71h ; q
.data:0040D259                 db  36h ; 6
.data:0040D25A                 db  6Ch ; l
.data:0040D25B                 db  19h
.data:0040D25C                 db 0E7h
.data:0040D25D                 db    6
.data:0040D25E                 db  6Bh ; k
.data:0040D25F                 db  6Eh ; n
.data:0040D260                 db  76h ; v
.data:0040D261                 db  1Bh
.data:0040D262                 db 0D4h
.data:0040D263                 db 0FEh
.data:0040D264                 db 0E0h
.data:0040D265                 db  2Bh ; +
.data:0040D266                 db 0D3h
.data:0040D267                 db  89h
.data:0040D268                 db  5Ah ; Z
.data:0040D269                 db  7Ah ; z
.data:0040D26A                 db 0DAh
.data:0040D26B                 db  10h
.data:0040D26C                 db 0CCh
.data:0040D26D                 db  4Ah ; J
.data:0040D26E                 db 0DDh
.data:0040D26F                 db  67h ; g
.data:0040D270                 db  6Fh ; o
.data:0040D271                 db 0DFh
.data:0040D272                 db 0B9h
.data:0040D273                 db 0F9h
.data:0040D274                 db 0F9h
.data:0040D275                 db 0EFh
.data:0040D276                 db 0BEh
.data:0040D277                 db  8Eh
.data:0040D278                 db  43h ; C
.data:0040D279                 db 0BEh
.data:0040D27A                 db 0B7h
.data:0040D27B                 db  17h
.data:0040D27C                 db 0D5h
.data:0040D27D                 db  8Eh
.data:0040D27E                 db 0B0h
.data:0040D27F                 db  60h ; `
.data:0040D280                 db 0E8h
.data:0040D281                 db 0A3h
.data:0040D282                 db 0D6h
.data:0040D283                 db 0D6h
.data:0040D284                 db  7Eh ; ~
.data:0040D285                 db  93h
.data:0040D286                 db 0D1h
.data:0040D287                 db 0A1h
.data:0040D288                 db 0C4h
.data:0040D289                 db 0C2h
.data:0040D28A                 db 0D8h
.data:0040D28B                 db  38h ; 8
.data:0040D28C                 db  52h ; R
.data:0040D28D                 db 0F2h
.data:0040D28E                 db 0DFh
.data:0040D28F                 db  4Fh ; O
.data:0040D290                 db 0F1h
.data:0040D291                 db  67h ; g
.data:0040D292                 db 0BBh
.data:0040D293                 db 0D1h
.data:0040D294                 db  67h ; g
.data:0040D295                 db  57h ; W
.data:0040D296                 db 0BCh
.data:0040D297                 db 0A6h
.data:0040D298                 db 0DDh
.data:0040D299                 db    6
.data:0040D29A                 db 0B5h
.data:0040D29B                 db  3Fh ; ?
.data:0040D29C                 db  4Bh ; K
.data:0040D29D                 db  36h ; 6
.data:0040D29E                 db 0B2h
.data:0040D29F                 db  48h ; H
.data:0040D2A0                 db 0DAh
.data:0040D2A1                 db  2Bh ; +
.data:0040D2A2                 db  0Dh
.data:0040D2A3                 db 0D8h
.data:0040D2A4                 db  4Ch ; L
.data:0040D2A5                 db  1Bh
.data:0040D2A6                 db  0Ah
.data:0040D2A7                 db 0AFh
.data:0040D2A8                 db 0F6h
.data:0040D2A9                 db  4Ah ; J
.data:0040D2AA                 db    3
.data:0040D2AB                 db  36h ; 6
.data:0040D2AC                 db  60h ; `
.data:0040D2AD                 db  7Ah ; z
.data:0040D2AE                 db    4
.data:0040D2AF                 db  41h ; A
.data:0040D2B0                 db 0C3h
.data:0040D2B1                 db 0EFh
.data:0040D2B2                 db  60h ; `
.data:0040D2B3                 db 0DFh
.data:0040D2B4                 db  55h ; U
.data:0040D2B5                 db 0DFh
.data:0040D2B6                 db  67h ; g
.data:0040D2B7                 db 0A8h
.data:0040D2B8                 db 0EFh
.data:0040D2B9                 db  8Eh
.data:0040D2BA                 db  6Eh ; n
.data:0040D2BB                 db  31h ; 1
.data:0040D2BC                 db  79h ; y
.data:0040D2BD                 db 0BEh
.data:0040D2BE                 db  69h ; i
.data:0040D2BF                 db  46h ; F
.data:0040D2C0                 db  8Ch
.data:0040D2C1                 db 0B3h
.data:0040D2C2                 db  61h ; a
.data:0040D2C3                 db 0CBh
.data:0040D2C4                 db  1Ah
.data:0040D2C5                 db  83h
.data:0040D2C6                 db  66h ; f
.data:0040D2C7                 db 0BCh
.data:0040D2C8                 db 0A0h
.data:0040D2C9                 db 0D2h
.data:0040D2CA                 db  6Fh ; o
.data:0040D2CB                 db  25h ; %
.data:0040D2CC                 db  36h ; 6
.data:0040D2CD                 db 0E2h
.data:0040D2CE                 db  68h ; h
.data:0040D2CF                 db  52h ; R
.data:0040D2D0                 db  95h
.data:0040D2D1                 db  77h ; w
.data:0040D2D2                 db  0Ch
.data:0040D2D3                 db 0CCh
.data:0040D2D4                 db    3
.data:0040D2D5                 db  47h ; G
.data:0040D2D6                 db  0Bh
.data:0040D2D7                 db 0BBh
.data:0040D2D8                 db 0B9h
.data:0040D2D9                 db  16h
.data:0040D2DA                 db    2
.data:0040D2DB                 db  22h ; "
.data:0040D2DC                 db  2Fh ; /
.data:0040D2DD                 db  26h ; &
.data:0040D2DE                 db    5
.data:0040D2DF                 db  55h ; U
.data:0040D2E0                 db 0BEh
.data:0040D2E1                 db  3Bh ; ;
.data:0040D2E2                 db 0BAh
.data:0040D2E3                 db 0C5h
.data:0040D2E4                 db  28h ; (
.data:0040D2E5                 db  0Bh
.data:0040D2E6                 db 0BDh
.data:0040D2E7                 db 0B2h
.data:0040D2E8                 db  92h
.data:0040D2E9                 db  5Ah ; Z
.data:0040D2EA                 db 0B4h
.data:0040D2EB                 db  2Bh ; +
.data:0040D2EC                 db    4
.data:0040D2ED                 db  6Ah ; j
.data:0040D2EE                 db 0B3h
.data:0040D2EF                 db  5Ch ; 
.data:0040D2F0                 db 0A7h
.data:0040D2F1                 db 0FFh
.data:0040D2F2                 db 0D7h
.data:0040D2F3                 db 0C2h
.data:0040D2F4                 db  31h ; 1
.data:0040D2F5                 db 0CFh
.data:0040D2F6                 db 0D0h
.data:0040D2F7                 db 0B5h
.data:0040D2F8                 db  8Bh
.data:0040D2F9                 db  9Eh
.data:0040D2FA                 db 0D9h
.data:0040D2FB                 db  2Ch ; ,
.data:0040D2FC                 db  1Dh
.data:0040D2FD                 db 0AEh
.data:0040D2FE                 db 0DEh
.data:0040D2FF                 db  5Bh ; [
.data:0040D300                 db 0B0h
.data:0040D301                 db 0C2h
.data:0040D302                 db  64h ; d
.data:0040D303                 db  9Bh
.data:0040D304                 db  26h ; &
.data:0040D305                 db 0F2h
.data:0040D306                 db  63h ; c
.data:0040D307                 db 0ECh
.data:0040D308                 db  9Ch
.data:0040D309                 db 0A3h
.data:0040D30A                 db  6Ah ; j
.data:0040D30B                 db  75h ; u
.data:0040D30C                 db  0Ah
.data:0040D30D                 db  93h
.data:0040D30E                 db  6Dh ; m
.data:0040D30F                 db    2
.data:0040D310                 db 0A9h
.data:0040D311                 db    6
.data:0040D312                 db    9
.data:0040D313                 db  9Ch
.data:0040D314                 db  3Fh ; ?
.data:0040D315                 db  36h ; 6
.data:0040D316                 db  0Eh
.data:0040D317                 db 0EBh
.data:0040D318                 db  85h
.data:0040D319                 db  67h ; g
.data:0040D31A                 db    7
.data:0040D31B                 db  72h ; r
.data:0040D31C                 db  13h
.data:0040D31D                 db  57h ; W
.data:0040D31E                 db    0
.data:0040D31F                 db    5
.data:0040D320                 db  82h
.data:0040D321                 db  4Ah ; J
.data:0040D322                 db 0BFh
.data:0040D323                 db  95h
.data:0040D324                 db  14h
.data:0040D325                 db  7Ah ; z
.data:0040D326                 db 0B8h
.data:0040D327                 db 0E2h
.data:0040D328                 db 0AEh
.data:0040D329                 db  2Bh ; +
.data:0040D32A                 db 0B1h
.data:0040D32B                 db  7Bh ; {
.data:0040D32C                 db  38h ; 8
.data:0040D32D                 db  1Bh
.data:0040D32E                 db 0B6h
.data:0040D32F                 db  0Ch
.data:0040D330                 db  9Bh
.data:0040D331                 db  8Eh
.data:0040D332                 db 0D2h
.data:0040D333                 db  92h
.data:0040D334                 db  0Dh
.data:0040D335                 db 0BEh
.data:0040D336                 db 0D5h
.data:0040D337                 db 0E5h
.data:0040D338                 db 0B7h
.data:0040D339                 db 0EFh
.data:0040D33A                 db 0DCh
.data:0040D33B                 db  7Ch ; |
.data:0040D33C                 db  21h ; !
.data:0040D33D                 db 0DFh
.data:0040D33E                 db 0DBh
.data:0040D33F                 db  0Bh
.data:0040D340                 db 0D4h
.data:0040D341                 db 0D2h
.data:0040D342                 db 0D3h
.data:0040D343                 db  86h
.data:0040D344                 db  42h ; B
.data:0040D345                 db 0E2h
.data:0040D346                 db 0D4h
.data:0040D347                 db 0F1h
.data:0040D348                 db 0F8h
.data:0040D349                 db 0B3h
.data:0040D34A                 db 0DDh
.data:0040D34B                 db  68h ; h
.data:0040D34C                 db  6Eh ; n
.data:0040D34D                 db  83h
.data:0040D34E                 db 0DAh
.data:0040D34F                 db  1Fh
.data:0040D350                 db 0CDh
.data:0040D351                 db  16h
.data:0040D352                 db 0BEh
.data:0040D353                 db  81h
.data:0040D354                 db  5Bh ; [
.data:0040D355                 db  26h ; &
.data:0040D356                 db 0B9h
.data:0040D357                 db 0F6h
.data:0040D358                 db 0E1h
.data:0040D359                 db  77h ; w
.data:0040D35A                 db 0B0h
.data:0040D35B                 db  6Fh ; o
.data:0040D35C                 db  77h ; w
.data:0040D35D                 db  47h ; G
.data:0040D35E                 db 0B7h
.data:0040D35F                 db  18h
.data:0040D360                 db 0E6h
.data:0040D361                 db  5Ah ; Z
.data:0040D362                 db    8
.data:0040D363                 db  88h
.data:0040D364                 db  70h ; p
.data:0040D365                 db  6Ah ; j
.data:0040D366                 db  0Fh
.data:0040D367                 db 0FFh
.data:0040D368                 db 0CAh
.data:0040D369                 db  3Bh ; ;
.data:0040D36A                 db    6
.data:0040D36B                 db  66h ; f
.data:0040D36C                 db  5Ch ; 
.data:0040D36D                 db  0Bh
.data:0040D36E                 db    1
.data:0040D36F                 db  11h
.data:0040D370                 db 0FFh
.data:0040D371                 db  9Eh
.data:0040D372                 db  65h ; e
.data:0040D373                 db  8Fh
.data:0040D374                 db  69h ; i
.data:0040D375                 db 0AEh
.data:0040D376                 db  62h ; b
.data:0040D377                 db 0F8h
.data:0040D378                 db 0D3h
.data:0040D379                 db 0FFh
.data:0040D37A                 db  6Bh ; k
.data:0040D37B                 db  61h ; a
.data:0040D37C                 db  45h ; E
.data:0040D37D                 db 0CFh
.data:0040D37E                 db  6Ch ; l
.data:0040D37F                 db  16h
.data:0040D380                 db  78h ; x
.data:0040D381                 db 0E2h
.data:0040D382                 db  0Ah
.data:0040D383                 db 0A0h
.data:0040D384                 db 0EEh
.data:0040D385                 db 0D2h
.data:0040D386                 db  0Dh
.data:0040D387                 db 0D7h
.data:0040D388                 db  54h ; T
.data:0040D389                 db  83h
.data:0040D38A                 db    4
.data:0040D38B                 db  4Eh ; N
.data:0040D38C                 db 0C2h
.data:0040D38D                 db 0B3h
.data:0040D38E                 db    3
.data:0040D38F                 db  39h ; 9
.data:0040D390                 db  61h ; a
.data:0040D391                 db  26h ; &
.data:0040D392                 db  67h ; g
.data:0040D393                 db 0A7h
.data:0040D394                 db 0F7h
.data:0040D395                 db  16h
.data:0040D396                 db  60h ; `
.data:0040D397                 db 0D0h
.data:0040D398                 db  4Dh ; M
.data:0040D399                 db  47h ; G
.data:0040D39A                 db  69h ; i
.data:0040D39B                 db  49h ; I
.data:0040D39C                 db 0DBh
.data:0040D39D                 db  77h ; w
.data:0040D39E                 db  6Eh ; n
.data:0040D39F                 db  3Eh ; >
.data:0040D3A0                 db  4Ah ; J
.data:0040D3A1                 db  6Ah ; j
.data:0040D3A2                 db 0D1h
.data:0040D3A3                 db 0AEh
.data:0040D3A4                 db 0DCh
.data:0040D3A5                 db  5Ah ; Z
.data:0040D3A6                 db 0D6h
.data:0040D3A7                 db 0D9h
.data:0040D3A8                 db  66h ; f
.data:0040D3A9                 db  0Bh
.data:0040D3AA                 db 0DFh
.data:0040D3AB                 db  40h ; @
.data:0040D3AC                 db 0F0h
.data:0040D3AD                 db  3Bh ; ;
.data:0040D3AE                 db 0D8h
.data:0040D3AF                 db  37h ; 7
.data:0040D3B0                 db  53h ; S
.data:0040D3B1                 db 0AEh
.data:0040D3B2                 db 0BCh
.data:0040D3B3                 db 0A9h
.data:0040D3B4                 db 0C5h
.data:0040D3B5                 db  9Eh
.data:0040D3B6                 db 0BBh
.data:0040D3B7                 db 0DEh
.data:0040D3B8                 db  7Fh ; 
.data:0040D3B9                 db 0CFh
.data:0040D3BA                 db 0B2h
.data:0040D3BB                 db  47h ; G
.data:0040D3BC                 db 0E9h
.data:0040D3BD                 db 0FFh
.data:0040D3BE                 db 0B5h
.data:0040D3BF                 db  30h ; 0
.data:0040D3C0                 db  1Ch
.data:0040D3C1                 db 0F2h
.data:0040D3C2                 db 0BDh
.data:0040D3C3                 db 0BDh
.data:0040D3C4                 db  8Ah
.data:0040D3C5                 db 0C2h
.data:0040D3C6                 db 0BAh
.data:0040D3C7                 db 0CAh
.data:0040D3C8                 db  30h ; 0
.data:0040D3C9                 db  93h
.data:0040D3CA                 db 0B3h
.data:0040D3CB                 db  53h ; S
.data:0040D3CC                 db 0A6h
.data:0040D3CD                 db 0A3h
.data:0040D3CE                 db 0B4h
.data:0040D3CF                 db  24h ; $
.data:0040D3D0                 db    5
.data:0040D3D1                 db  36h ; 6
.data:0040D3D2                 db 0D0h
.data:0040D3D3                 db 0BAh
.data:0040D3D4                 db  93h
.data:0040D3D5                 db    6
.data:0040D3D6                 db 0D7h
.data:0040D3D7                 db 0CDh
.data:0040D3D8                 db  29h ; )
.data:0040D3D9                 db  57h ; W
.data:0040D3DA                 db 0DEh
.data:0040D3DB                 db  54h ; T
.data:0040D3DC                 db 0BFh
.data:0040D3DD                 db  67h ; g
.data:0040D3DE                 db 0D9h
.data:0040D3DF                 db  23h ; #
.data:0040D3E0                 db  2Eh ; .
.data:0040D3E1                 db  7Ah ; z
.data:0040D3E2                 db  66h ; f
.data:0040D3E3                 db 0B3h
.data:0040D3E4                 db 0B8h
.data:0040D3E5                 db  4Ah ; J
.data:0040D3E6                 db  61h ; a
.data:0040D3E7                 db 0C4h
.data:0040D3E8                 db    2
.data:0040D3E9                 db  1Bh
.data:0040D3EA                 db  68h ; h
.data:0040D3EB                 db  5Dh ; ]
.data:0040D3EC                 db  94h
.data:0040D3ED                 db  2Bh ; +
.data:0040D3EE                 db  6Fh ; o
.data:0040D3EF                 db  2Ah ; *
.data:0040D3F0                 db  37h ; 7
.data:0040D3F1                 db 0BEh
.data:0040D3F2                 db  0Bh
.data:0040D3F3                 db 0B4h
.data:0040D3F4                 db 0A1h
.data:0040D3F5                 db  8Eh
.data:0040D3F6                 db  0Ch
.data:0040D3F7                 db 0C3h
.data:0040D3F8                 db  1Bh
.data:0040D3F9                 db 0DFh
.data:0040D3FA                 db    5
.data:0040D3FB                 db  5Ah ; Z
.data:0040D3FC                 db  8Dh
.data:0040D3FD                 db 0EFh
.data:0040D3FE                 db    2
.data:0040D3FF                 db  2Dh ; -
.data:0040D400                 db    0
.data:0040D401                 db    0
.data:0040D402                 db    0
.data:0040D403                 db    0
.data:0040D404                 db    0
.data:0040D405                 db    0
.data:0040D406                 db    0
.data:0040D407                 db    0
.data:0040D408                 db    0
.data:0040D409                 db    0
.data:0040D40A                 db    0
.data:0040D40B                 db    0
.data:0040D40C                 db    0
.data:0040D40D                 db    0
.data:0040D40E                 db    0
.data:0040D40F                 db    0
"""

# Split the input text into lines
lines = input_text.split('\n')
counter  = 0
result_list = [line.split('db')[1].split(';')[0].strip().rstrip('h') for line in lines if 'db' in line]

def process_input(input_char, dw40D410):
    # Take the ASCII value of the input character
    ascii_value = ord(input_char)
    # XOR it with FFFFFFFF
    xor_result = ascii_value ^ dw40D410 
    # print(format(xor_result,'08X'))
    # Take the result and 000000FF
    and_result = xor_result & 0x000000FF
    # print("ecx:", format(and_result, '08X'))
    
    ecx_40D000 = result_list[(and_result*4)-4 : (and_result*4)]
    # print(result_list[(and_result*4)-4 : (and_result*4)])
    int_values = [int(hex_str, 16) for hex_str in ecx_40D000]
    combined_hex = (int_values[3] << 24) | (int_values[2] << 16) | (int_values[1] << 8) | int_values[0]
    # print("dword [40D000] = ",format(combined_hex,'08X'))
    # SHR that, 8
    nextSHR = dw40D410 >> 8
    final_result = nextSHR ^ combined_hex
    dw40D410 = final_result
    # print("Result:", format(final_result, '08X'))
    return final_result

# Example with input "a"
input_char = input("Enter your name (at least 3 characters): ")
if len(input_char) == 3:
    result = "@" + input_char

dw40D410 = 0xFFFFFFFF
for char in input_char:
    dw40D410 = process_input(char, dw40D410)

# print("Final Result after all iterations:", format(dw40D410, '08X'))
higher_part = (dw40D410 >> 16) & 0xFFFF
lower_part = dw40D410 & 0xFFFF

# Calculate the modulus and add 256 to the remainder for the higher part
_40DE3E8 =  int((higher_part % 8198) + 256)
_40DE3F0 =  int((lower_part % 8198) + 256)
# Print the result
# print("[40DE3E8]:", format(_40DE3E8)  )
# print("[40DE3F0]]:", format(_40DE3F0)  )

x1, x3 = symbols('x1 x3')

# Given equations
equation2 = Eq(x1**2 + x3**2, 65536)
equation1 = Eq((_40DE3F0 - x3) / ((_40DE3E8 - x1)) * x3 / x1, -1)
    

# Solve the system of equations
solutions = solve((equation1, equation2), (x1, x3))

# Print the solutions
# print("Solutions where x3 is below 0:")
for solution in solutions:
    x1_value = int(float(solution[0]) * 1000000)
    x3_value = int(float(solution[1]) * 1000000)
    if x3_value < 0:
        # print(f"x1 = {x1_value:.6f}, x3 = {x3_value:.6f}")
        
        # Convert to 32-bit signed integer and then to hexadecimal
        x1_hex = format(int(x1_value) & 0xFFFFFFFF, '08X')
        x3_hex = format(int(x3_value) & 0xFFFFFFFF, '08X')
        
        # print(f"x1 in hex: {x1_hex}")
        # print(f"x3 in hex: {x3_hex}")
        print(x1_hex + "-" + x1_hex + "-" + x3_hex + "-" + x3_hex)
   