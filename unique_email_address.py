from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        final = set()
        for email in emails:
            if '+' in email:
                first_index = email.index('+')
                second_index = email.index("@")
                email = email.replace(email[first_index:second_index], "")
            before, after = email.split("@")

            before = before.replace('.', '')

            email = before + '@' + after
            final.add(email)
        return len(final)


s = Solution()
print(s.numUniqueEmails(["fg.r.u.uzj+o.pw@kziczvh.com","r.cyo.g+d.h+b.ja@tgsg.z.com",
                         "fg.r.u.uzj+o.f.d@kziczvh.com","r.cyo.g+ng.r.iq@tgsg.z.com",
                         "fg.r.u.uzj+lp.k@kziczvh.com","r.cyo.g+n.h.e+n.g@tgsg.z.com","fg.r.u.uzj+k+p.j@kziczvh.com","fg.r.u.uzj+w.y+b@kziczvh.com","r.cyo.g+x+d.c+f.t@tgsg.z.com","r.cyo.g+x+t.y.l.i@tgsg.z.com","r.cyo.g+brxxi@tgsg.z.com","r.cyo.g+z+dr.k.u@tgsg.z.com","r.cyo.g+d+l.c.n+g@tgsg.z.com","fg.r.u.uzj+vq.o@kziczvh.com","fg.r.u.uzj+uzq@kziczvh.com",
                         "fg.r.u.uzj+mvz@kziczvh.com","fg.r.u.uzj+taj@kziczvh.com",
                         "fg.r.u.uzj+fek@kziczvh.com"]))
