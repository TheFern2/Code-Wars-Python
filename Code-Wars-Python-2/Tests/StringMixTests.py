import unittest
from StringMix import mix
from StringMix import mix2
from StringMix import mix3

class StringMixTest(unittest.TestCase):
    def test(self):
        self.assertEqual(mix2("mmmmm m nnnnn y&friend&Paul has heavy hats! &", "my frie n d Joh n has ma n y ma n y frie n ds n&"), "1:mmmmmm/=:nnnnnn/1:aaaa/1:hhh/2:yyy/2:dd/2:ff/2:ii/2:rr/=:ee/=:ss")
        self.assertEqual(mix2("Are they here", "yes, they are here"), "2:eeeee/2:yy/=:hh/=:rr")
        self.assertEqual(mix2("looping is fun but dangerous", "less dangerous than coding"), "1:ooo/1:uuu/2:sss/=:nnn/1:ii/2:aa/2:dd/2:ee/=:gg")
        self.assertEqual(mix2(" In many languages", " there's a pair of functions"), "1:aaa/1:nnn/1:gg/2:ee/2:ff/2:ii/2:oo/2:rr/2:ss/2:tt")
        self.assertEqual(mix2("Lords of the Fallen", "gamekult"), "1:ee/1:ll/1:oo")
        self.assertEqual(mix2("codewars", "codewars"), "")
        self.assertEqual(mix2("A generation must confront the looming ", "codewarrs"), "1:nnnnn/1:ooooo/1:tttt/1:eee/1:gg/1:ii/1:mm/=:rr")
        self.assertEqual(mix2("NtytbByvdxShwbv6ozzk/gwow?fqbz", "KdexbUpozl%qmjaLegqpJjdpk+bylb"), "1:www/1:zzz/2:ppp/=:bbb/1:oo/1:tt/1:vv/1:yy/2:dd/2:ee/2:jj/2:ll/2:qq")
        self.assertEqual(mix2("FuwrpTwbic5srynVxthf'imez%unvk", "&egvkLpdry=ppjnWwduqKjvrr&swou"), "2:ppp/2:rrr/1:ii/1:nn/2:dd/2:jj/2:vv/=:uu/=:ww")
        self.assertEqual(mix2("7xmho/ctid,spgj?hjraIixto&wtpm", "Qoypx0bzyu4znwy5odkmPmmtp.wlrj"), "1:ttt/2:mmm/2:yyy/1:hh/1:ii/1:jj/1:xx/2:ww/2:zz/=:oo/=:pp")
        self.assertEqual(mix2("+gumoIkqgiZzjom3zpgk4tpboEqxkk", "7rttpLmzybQiick&bbgyDxmcuQrkym"), "1:kkkk/1:ggg/1:ooo/2:bbb/2:mmm/2:yyy/1:pp/1:qq/1:zz/2:cc/2:ii/2:rr/2:tt")
        self.assertEqual(mix2("FtnlkSgprn9cdrb:gflu+zhmm1lemw", "*gapyVoxhuSpikuDghiyTbtlrOojgp"), "1:lll/1:mmm/2:ggg/2:ppp/1:nn/1:rr/2:hh/2:ii/2:oo/2:uu/2:yy")