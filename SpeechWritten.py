def fetch_rules():
    rules={"number":{"zero":0,"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,
                 "nine":9,"ten":10,"twenty":20,"thirty":30,"forty":40,"fifty":50,"sixty":60,"seventy":70,
                 "eighty":80,"ninety":90,"hundred":100,"thousand":1000,"million":1000000},
          "tuple":{"single":0,"double":2,"triple":3,"quadruple":4,"quintuple":5,"sextuple":6,"septuple":7,"octuple":8,"nonuple":9,"decuple":10}}
    return rules

class SpeechWritten:
    def __init__(self):
        self.rules=fetch_rules()
        self.ip=""
        self.op=""

    def get_ip(self):
        self.ip=input("Enter your paragraph:")
        if not self.ip:
            print("\nYou entered nothing")

    def show_op(self):
        print("\nyour output is: "+self.op)

    def convert(self):
        words=self.ip.split()

        num=self.rules['number']
        tup=self.rules['tuple']

        i=0
        c=0
        n=len(words)

        while i<n:
            if (len(words[i])==1):
                if c==0 and i!=0:
                    self.op=self.op+" "
                    c=1
                self.op=self.op+words[i]
                i+=1
            elif i+1 != n:
                c=0
                if words[i].lower() in num.keys() and (words[i+1].lower()=='dollar' or words[i+1].lower()=='dollars'):
                    self.op=self.op+" $"+str(num[words[i].lower()])
                    i+=2
                elif words[i].lower() in tup.keys() and len(words[i+1])==1:
                    self.op=self.op+" "+words[i+1]*tup[words[i].lower()]
                    i+=2
                else:
                    self.op=self.op+" "+words[i]
                    i+=1
            else:
                c=0
                self.op=self.op+" "+words[i]
                i+=1

def main():
    obj=SpeechWritten()
    obj.get_ip()
    obj.convert()
    obj.show_op()
