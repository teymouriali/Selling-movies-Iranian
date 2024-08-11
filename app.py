import requests
from bs4 import BeautifulSoup

k = 0
lisname = []
lisnamedirector = []
lisprice = []

url = "https://iticket.ir/box-office"
response = requests.get(url)


def main():
    if response.status_code == 200:

        soap = BeautifulSoup(response.text, "html.parser")

        j = soap.find_all("p", attrs={
            "class": "text-primary text-[0.81rem] font-semibold leading-[1.125rem]"})

        t = soap.find_all("p", attrs={
            "class": "text-gray-1 text-[0.69rem] font-regular leading-[1.09375rem]"})

        p = soap.find_all("p", attrs={"class": "text-primary text-end"})

        for k in range(int(len(j))):
            for i in p[k]:
                k += 1
                lisprice.append(i)

        for k in range(int(len(j))):
            for i in j[k]:
                k += 1
                lisname.append(i)

        for k in range(int(len(j))):
            for i in t[k]:
                k += 1
                lisnamedirector.append(i)

        fin = list(zip(lisname, lisnamedirector, lisprice))

        for w, xx, yy in fin:

            if len(xx) == 1:
                xx = "نام کارگردان ذکر نشده"
            print("نام فیلم:"+str(w).strip(), "نام کارگردان:"+str(xx).strip(), "فروش کل :" + str(
                yy).strip(), sep=" = ", flush=True, end="\n"*2)


if __name__ == "__main__":
    main()
