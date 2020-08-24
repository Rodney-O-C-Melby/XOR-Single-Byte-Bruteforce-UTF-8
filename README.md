# XOR-Single-Byte-Bruteforce-UTF-8
Brute force Strings using XOR, chosen key of length one, and UTF-8 encoding.

Written for a CTF - Single Byte XOR Calculator - no error checking or unit tests

Depends: Python 3.7

<code>Usage: python xor-bruteforce.py</code>

The program encrypts each message with the key 'R' and then performs an XOR bitwise operation twice, once to encrypt, twice to decrypt. Lastly the 'bruteforce' method checks all possible printable combinations for each possible key of length one for any given ciphertext. (checks all letters and numbers as the key for decryption)

Example execution

<code>python xor-bruteforce.py</code>
<code>
Cleartext Message: Single Byte XOR encryption and decryption example python 3.7

Encryption Key: R

Encrypted Message: ;<5>7r+&7r
r7<1 +"&;=<r3<6r671 +"&;=<r7*3?">7r"+&:=<ra|e

Encryption Success.

Decrypted Message: Single Byte XOR encryption and decryption example python 3.7

Decryption Success.

Brute Force ASSCII chars and print valid results:

70 G}zsxq4Vm`q4L[F4qzwfmd`}{z4uzp4pqwfmd`}{z4qluydxq4dm`|{z4':#

71 F|{ryp5Wlap5MZG5p{vglea|z{5t{q5qpvglea|z{5pmtxeyp5ela}z{5&;"

75 Jpw~u|9[`m|9AVK9|wzk`impvw9xw}9}|zk`impvw9|axtiu|9i`mqvw9*7.

77 Lvqxsz?]fkz?GPM?zq|mfokvpq?~q{?{z|mfokvpq?zg~rosz?ofkwpq?,1(

79 Ntszqx=_dix=ERO=xs~odmitrs=|sy=yx~odmitrs=xe|pmqx=mdiurs=.3*

80 Qkleng"@{vg"ZMP"glap{rvkml"clf"fgap{rvkml"gzcorng"r{vjml"1,5

81 Pjmdof#Azwf#[LQ#fm`qzswjlm#bmg#gf`qzswjlm#f{bnsof#szwklm#0-4

82 Single Byte XOR encryption and decryption example python 3.7

83 Rhofmd!Cxud!YNS!dobsxquhno!`oe!edbsxquhno!dy`lqmd!qxuino!2/6

86 Wmjcha$F}pa$\KV$ajgv}tpmkj$ej`$`agv}tpmkj$a|eitha$t}plkj$7*3

87 Vlkbi`%G|q`%]JW%`kfw|uqljk%dka%a`fw|uqljk%`}dhui`%u|qmjk%6+2

88 Ycdmfo*Hs~o*REX*odixsz~ced*kdn*noixsz~ced*orkgzfo*zs~bed*9$=

90 [afodm(Jq|m(PGZ(mfkzqx|agf(ifl(lmkzqx|agf(mpiexdm(xq|`gf(;&?

91 Z`gnel)Kp}l)QF[)lgj{py}`fg)hgm)mlj{py}`fg)lqhdyel)yp}afg):'>

92 ]g`ibk.Lwzk.VA\.k`m|w~zga`.o`j.jkm|w~zga`.kvoc~bk.~wzfa`.= 9

94 _ebk`i,Nuxi,TC^,ibo~u|xecb,mbh,hio~u|xecb,itma|`i,|uxdcb,?";

192 Áûüõþ÷²Ðëæ÷²ÊÝÀ²÷üñàëâæûýü²óüö²ö÷ñàëâæûýü²÷êóÿâþ÷²âëæúýü²¡¼¥

194 Ãùþ÷üõ°Òéäõ°ÈßÂ°õþóâéàäùÿþ°ñþô°ôõóâéàäùÿþ°õèñýàüõ°àéäøÿþ°£¾§

195 Âøÿöýô±Óèåô±ÉÞÃ±ôÿòãèáåøþÿ±ðÿõ±õôòãèáåøþÿ±ôéðüáýô±áèåùþÿ±¢¿¦

196 Åÿøñúó¶Ôïâó¶ÎÙÄ¶óøõäïæâÿùø¶÷øò¶òóõäïæâÿùø¶óî÷ûæúó¶æïâþùø¶¥¸¡

198 Çýúóøñ´Öíàñ´ÌÛÆ´ñú÷æíäàýûú´õúð´ðñ÷æíäàýûú´ñìõùäøñ´äíàüûú´§º£

199 Æüûòùðµ×ìáðµÍÚÇµðûöçìåáüúûµôûñµñðöçìåáüúûµðíôøåùðµåìáýúûµ¦»¢

201 Èòõü÷þ»Ùâïþ»ÃÔÉ»þõøéâëïòôõ»úõÿ»ÿþøéâëïòôõ»þãúöë÷þ»ëâïóôõ»¨µ¬

202 Ëñöÿôý¸Úáìý¸À×Ê¸ýöûêáèìñ÷ö¸ùöü¸üýûêáèìñ÷ö¸ýàùõèôý¸èáìð÷ö¸«¶¯

203 Êð÷þõü¹Ûàíü¹ÁÖË¹ü÷úëàéíðö÷¹ø÷ý¹ýüúëàéíðö÷¹üáøôéõü¹éàíñö÷¹ª·®

205 Ìöñøóú¿Ýæëú¿ÇÐÍ¿úñüíæïëöðñ¿þñû¿ûúüíæïëöðñ¿úçþòïóú¿ïæë÷ðñ¿¬±¨

206 Ïõòûðù¼Þåèù¼ÄÓÎ¼ùòÿîåìèõóò¼ýòø¼øùÿîåìèõóò¼ùäýñìðù¼ìåèôóò¼¯²«

207 Îôóúñø½ßäéø½ÅÒÏ½øóþïäíéôòó½üóù½ùøþïäíéôòó½øåüðíñø½íäéõòó½®³ª

208 Ñëìåîç¢Àûöç¢ÚÍÐ¢çìáðûòöëíì¢ãìæ¢æçáðûòöëíì¢çúãïòîç¢òûöêíì¢±¬µ

211 Òèïæíä¡Ãøõä¡ÙÎÓ¡äïâóøñõèîï¡àïå¡åäâóøñõèîï¡äùàìñíä¡ñøõéîï¡²¯¶

212 Õïèáêã¦Äÿòã¦ÞÉÔ¦ãèåôÿöòïéè¦çèâ¦âãåôÿöòïéè¦ãþçëöêã¦öÿòîéè¦µ¨±

213 Ôîéàëâ§Åþóâ§ßÈÕ§âéäõþ÷óîèé§æéã§ãâäõþ÷óîèé§âÿæê÷ëâ§÷þóïèé§´©°

214 ×íêãèá¤Æýðá¤ÜËÖ¤áêçöýôðíëê¤åêà¤àáçöýôðíëê¤áüåéôèá¤ôýðìëê¤·ª³

215 Öìëâéà¥Çüñà¥ÝÊ×¥àëæ÷üõñìêë¥äëá¥áàæ÷üõñìêë¥àýäèõéà¥õüñíêë¥¶«²

216 ÙãäíæïªÈóþïªÒÅØªïäéøóúþãåäªëäîªîïéøóúþãåäªïòëçúæïªúóþâåäª¹¤½

217 Øâåìçî«Éòÿî«ÓÄÙ«îåèùòûÿâäå«êåï«ïîèùòûÿâäå«îóêæûçî«ûòÿãäå«¸¥¼

218 Ûáæïäí¨Êñüí¨ÐÇÚ¨íæëúñøüáçæ¨éæì¨ìíëúñøüáçæ¨íðéåøäí¨øñüàçæ¨»¦¿

219 Úàçîåì©Ëðýì©ÑÆÛ©ìçêûðùýàæç©èçí©íìêûðùýàæç©ìñèäùåì©ùðýáæç©º§¾

221 Üæáèãê¯Íöûê¯×ÀÝ¯êáìýöÿûæàá¯îáë¯ëêìýöÿûæàá¯ê÷îâÿãê¯ÿöûçàá¯¼¡¸

222 ßåâëàé¬Îõøé¬ÔÃÞ¬éâïþõüøåãâ¬íâè¬èéïþõüøåãâ¬éôíáüàé¬üõøäãâ¬¿¢»

</code>
