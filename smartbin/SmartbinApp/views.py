from django.shortcuts import render,HttpResponse,HttpResponseRedirect
import MySQLdb
import datetime
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
import simplejson as json
from datetime import date
from datetime import datetime
import datetime
import webbrowser
import math, random 

def sendsms(ph,msg):
    sendToPhoneNumber= "+91"+ph
    userid = "2000022557"
    passwd = "54321@lcc"
    url = "http://enterprise.smsgupshup.com/GatewayAPI/rest?method=sendMessage&send_to=" + sendToPhoneNumber + "&msg=" + msg + "&userid=" + userid + "&password=" + passwd + "&v=1.1&msg_type=TEXT&auth_scheme=PLAIN"
    # contents = urllib.request.urlopen(url)
    webbrowser.open(url)

def generateOTP() :   
    # Declare a digits variable   
    # which stores all digits  
    digits = "0123456789"
    OTP = "" 
   # length of password can be chaged 
   # by changing value in range 
    for i in range(4) : 
        OTP += digits[math.floor(random.random() * 10)] 
        print(i)
    return OTP 

# Create your views here.

db = MySQLdb.connect('localhost','root','','smartbin_db')
c = db.cursor()

def AdminHome(request):
    return render(request,'AdminHome.html') 

def CommonHome(request):
    return render(request,'CommonHome.html')

def CustomerHome(request):
    return render(request,'CustomerHome.html')

def SignIn(request):  
    request.session['username']=""
    request.session['NAME']=""
    request.session['cid']=""
    msg=""
    if request.POST:
        email = request.POST.get("email")
        password = request.POST.get("password")
        c.execute("select * from login where uname='"+ email +"' and pass='"+ password +"'")
        ds = c.fetchone()
        print(ds)
        request.session['username']=email
        if ds is not None:
            if ds[2] == 'Admin':
                return HttpResponseRedirect('/AdminHome/')
            elif ds[2] == 'Customer':
                c.execute("select * from cust_reg where email='"+email+"' and password='"+password+"'")
                ds = c.fetchone()
                request.session['cid'] = ds[0]
                request.session['NAME'] = ds[1]
                return HttpResponseRedirect('/CustomerHome/')
            elif ds[2] == 'Authority':
                c.execute("select * from `authority_reg` where email='"+email+"' and password='"+password+"'")
                ds = c.fetchone()
                request.session['cid'] = ds[0]
                request.session['NAME'] = ds[1]
                return HttpResponseRedirect('/AutorityAddWaste/')
            elif ds[2] == 'Muncipality':
                c.execute("select * from `muncipality_reg` where email='"+email+"' and password='"+password+"'")
                ds = c.fetchone()
                request.session['cid'] = ds[0]
                request.session['NAME'] = ds[1]
                return HttpResponseRedirect('/MuncipalityViewWaste/')
        else:
            msg="Incorrect Username or Password"
        
    return render(request,'Signin.html',{"msg":msg}) 

def MuncipalitySignUp(request):
    msg = ""
    if request.POST:
        cname = request.POST.get("cname")
        address = request.POST.get("address")
        cntry = request.POST.get("district")
        state = request.POST.get("location")
        fon = request.POST.get("mobile")
        email = request.POST.get("Email")
        password = request.POST.get("Password")
        type= "Muncipality"
        qry="insert into Muncipality_reg(cname,address,district,location,mobile,email,password) values('"+ str(cname) +"','"+ str(address) +"','"+ str(cntry) +"','"+ str(state) +"','"+ str(fon) +"','"+ str(email) +"','"+ str(password) +"')"
        qr ="insert into login values('"+ str(email) +"','"+ str(password) +"','"+ type +"')"
        c.execute(qry)
        c.execute(qr)
        db.commit()
        msg = "Registartion Completed Successfully."
    return render(request,'MuncipalitySignUp.html',{"msg":msg})

def AuthoritySignUp(request):
    msg = ""
    if request.POST:
        cname = request.POST.get("cname")
        address = request.POST.get("address")
        cntry = request.POST.get("district")
        state = request.POST.get("location")
        fon = request.POST.get("mobile")
        email = request.POST.get("Email")
        password = request.POST.get("Password")
        type= "Authority"
        qry="insert into Authority_reg(cname,address,district,location,mobile,email,password) values('"+ str(cname) +"','"+ str(address) +"','"+ str(cntry) +"','"+ str(state) +"','"+ str(fon) +"','"+ str(email) +"','"+ str(password) +"')"
        qr ="insert into login values('"+ str(email) +"','"+ str(password) +"','"+ type +"')"
        c.execute(qry)
        c.execute(qr)
        db.commit()
        msg = "Registartion Completed Successfully."
    return render(request,'AuthoritySignUp.html',{"msg":msg})

def CustomerSignUp(request):
    msg = ""
    if request.POST:
        cname = request.POST.get("name")
        address = request.POST.get("adrs")
        cntry = request.POST.get("cntry")
        state = request.POST.get("state")
        fon = request.POST.get("fon")
        email = request.POST.get("email")
        password = request.POST.get("pass")
        type= "Customer"
        qry="insert into cust_reg(cname,address,district,location,mobile,email,password) values('"+str(cname)+"','"+str(address)+"','"+str(cntry)+"','"+str(state)+"','"+str(fon)+"','"+str(email)+"','"+str(password)+"')"
        qr ="insert into login values('"+str(email)+"','"+str(password)+"','"+(type)+"')"
        c.execute(qry)
        c.execute(qr)
        db.commit()
        msg = "Registartion Completed Successfully."
    return render(request,'CustomerSignUp.html',{"msg":msg})

def AdminAddCategory(request):
    msg=""
    if request.POST:
        na = request.POST.get("cat_name")
        qry="insert into categories(catname) values('"+ na +"')"
        c.execute(qry)
        db.commit()
        msg = "Category Added Successfully."
    c.execute("select * from categories")
    data=c.fetchall() 
    if request.GET:
        a = request.GET.get('id')
        c.execute("delete from categories where catid = '"+str(a)+"'")
        db.commit()
        return HttpResponseRedirect("/AdminAddCategory/")
    return render(request,'AdminAddCategory.html',{"data":data,"msg":msg})
def AdminAddBin(request):
    msg=""
    if request.POST:
        types = request.POST.get("type")
        size = request.POST.get("type")
        qry="insert into bintable(bintype,binsize) values('"+ types +"','"+size+"')"
        c.execute(qry)
        db.commit()
        msg = "Bin Added Successfully."
    c.execute("select * from bintable")
    data=c.fetchall() 
    if request.GET:
        a = request.GET.get('id')
        c.execute("delete from bintable where id = '"+str(a)+"'")
        db.commit()
        return HttpResponseRedirect("/AdminAddBin/")
    return render(request,'AdminAddBin.html',{"data":data,"msg":msg})

def AdminAddSubCategory(request):
    msg=""
    if request.POST:
        ca = request.POST.get("cat_title")
        sc = request.POST.get("cat_name")
        qry="insert into subcategory(catid,sname) values('"+ ca +"','"+sc+"')"
        c.execute(qry)
        db.commit()
        msg = "Subcategory Added Successfully."
    c.execute("select * from categories")
    data=c.fetchall() 
    c.execute("select * from subcategory")
    sdata=c.fetchall()
    if request.GET:
        a = request.GET.get('id')
        c.execute("delete from subcategory where sid = '"+str(a)+"'")
        db.commit()
        return HttpResponseRedirect("/AdminAddSubCategory/")
    return render(request,'AdminAddSubCategory.html',{"data":data,"msg":msg,"sdata":sdata})

def AdminAddEvents(request):
    msg=""
    if request.POST:
        na = request.POST.get("cat_name")
        qry="insert into events(events) values('"+ na +"')"
        c.execute(qry)
        db.commit()
        msg = "Events Added Successfully."
    c.execute("select * from events")
    data=c.fetchall() 
    if request.GET:
        a = request.GET.get('id')
        c.execute("delete from events where eid = '"+str(a)+"'")
        db.commit()
        return HttpResponseRedirect("/AdminAddEvents/")
    return render(request,'AdminAddEvents.html',{"data":data,"msg":msg})

def CustomerAddEvents(request):
    msg=""
    if request.POST:
        na = request.POST.get("ename")
        place = request.POST.get("place")
        address = request.POST.get("address")
        date = request.POST.get("date")
    
        qry="insert into custevents(Eventname,Place,Address,date) values('"+str(na) +"','"+str(place)+"','"+str(address)+"','"+str(date)+"')"
        c.execute(qry)
        db.commit()
        msg = "Events Added Successfully."
    c.execute("select * from custevents")
    data=c.fetchall() 
    if request.GET:
        a = request.GET.get('id')
        c.execute("delete from custevents where eid = '"+str(a)+"'")
        db.commit()
        return HttpResponseRedirect("/CustomerAddEvents/")
    return render(request,'CustomerAddEvents.html',{"data":data,"msg":msg})

def CustomerAddFood(request):
    msg=""
    c.execute("select * from events")
    data1=c.fetchall() 
    if request.POST:
        na = request.POST.get("ename")
        place = request.POST.get("place")
        address = request.POST.get("address")
        date = request.POST.get("date")

        qry="insert into customerfood(eventid,qty,quality,date) values('"+ str(na) +"','"+str(place)+"','"+str(address)+"','"+str(date)+"')"
        c.execute(qry)
        db.commit()
        msg = "Events Added Successfully."
    c.execute("select * from customerfood")
    data=c.fetchall() 
    if request.GET:
        a = request.GET.get('id')
        c.execute("delete from customerfood where fid = '"+str(a)+"'")
        db.commit()
        return HttpResponseRedirect("/CustomerAddEvents/")
    return render(request,'CustomerAddFood.html',{"data":data,"msg":msg,"data1":data1})
def AutorityAddWaste(request):
    msg=""
    
    if request.POST:
        types = request.POST.get("type")
        qty = request.POST.get("qty")
        location = request.POST.get("location")
        date = request.POST.get("date")

        qry="insert into wastetable(type,qty,location,date) values('"+ str(types) +"','"+str(qty)+"','"+str(location)+"','"+str(date)+"')"
        c.execute(qry)
        db.commit()
        msg = "Events Added Successfully."
    c.execute("select * from wastetable")
    data=c.fetchall() 
    if request.GET:
        a = request.GET.get('id')
        c.execute("delete from wastetable where id = '"+str(a)+"'")
        db.commit()
        return HttpResponseRedirect("/AutorityAddWaste/")
    return render(request,'AuthorityAddWaste.html',{"data":data,"msg":msg})
def AdminAddProduct(request):
    c.execute("select * from categories")
    data=c.fetchall()
    c.execute("select * from events")
    edata=c.fetchall()
    msg=""  
    if request.POST:
        a=request.POST.get("cat")
        b=request.POST.get("subcategory")
        c.execute("select sid from subcategory where sname = '"+b+"'")
        sub = c.fetchone()
        subid = sub[0]
        c1=request.POST.get("event")   
        d=request.POST.get('product_title')
        e=request.POST.get("des")
        f=request.POST.get("price")   
        qty = request.POST.get("qty")
        if request.FILES.get("file"):
            myfile=request.FILES.get("file")
            fs=FileSystemStorage()
            filename=fs.save(myfile.name , myfile)
            uploaded_file_url = fs.url(filename)
            c.execute("insert into products(catid,subid,evid,pname,pdesc,pimage,pamount,qty) values('"+ str(a) +"','"+ str(subid) +"','"+ str(c1) +"','"+str(d)+"','"+str(e)+"','"+ str(uploaded_file_url) +"','"+ str(f) +"','"+qty+"')")
            db.commit()       
            msg = "Products Added Successfully."
    return render(request,"AdminAddProduct.html",{"cat":data,"msg":msg,"edata":edata})
def AdminAddBintoMunicipality(request):
    c.execute("select * from bintable")
    data=c.fetchall()
    c.execute("select * from `muncipality_reg`")
    edata=c.fetchall()
    msg=""  
    if request.POST:
        
        typed=request.POST.get('type')
        mname=request.POST.get("mname")
        d=date.today()
        qty = request.POST.get("qty")
        c.execute("insert into `adminaddbintomuncipality`(Binid,muncipalityid,qty,date) values('"+ str(typed) +"','"+ str(mname) +"','"+ str(qty) +"','"+str(d)+"')")
        db.commit()       
        msg = "Products Added Successfully."
    return render(request,"AdminAddBintoMunicipality.html",{"cat":data,"msg":msg,"edata":edata})

def AdminViewCustomers(request):
    data = ""
    c.execute("select * from cust_reg")
    data=c.fetchall() 
    return render (request,"AdminViewCustomers.html",{"data":data})
def AdminViewMuncipality(request):
    data = ""
    c.execute("select * from muncipality_reg")
    data=c.fetchall() 
    return render (request,"AdminViewMuncipality.html",{"data":data})
def AdminViewAuthority(request):
    data = ""
    c.execute("select * from authority_reg")
    data=c.fetchall() 
    return render (request,"AdminViewAuthority.html",{"data":data})
def AdminViewWaste(request):
    data = ""
    c.execute("select * from wastetable")
    data=c.fetchall() 
    return render (request,"AdminViewWaste.html",{"data":data})
def MuncipalityViewWaste(request):
    data = ""
    c.execute("select * from wastetable")
    data=c.fetchall() 
    return render (request,"MuncipalityViewWaste.html",{"data":data})
def MuncipalityViewFood(request):
    data = ""
    c.execute("select * from CustomerFood")
    data=c.fetchall() 
    return render (request,"MuncipalityViewFood.html",{"data":data})
def MuncipalityViewevents(request):
    data = ""
    c.execute("select * from custevents")
    data=c.fetchall() 
    return render (request,"MuncipalityViewevents.html",{"data":data})
def AutorityViewevents(request):
    data = ""
    c.execute("select * from custevents")
    data=c.fetchall() 
    return render (request,"AutorityViewevents.html",{"data":data})
def AuthorityViewFood(request):
    data = ""
    c.execute("select * from CustomerFood")
    data=c.fetchall() 
    return render (request,"AuthorityViewFood.html",{"data":data})

def AdminViewFeedback(request):
    data = ""
    c.execute("select * from cust_reg inner join feedback on cust_reg.cid = feedback.cid")
    data=c.fetchall() 
    return render (request,"AdminViewFeedback.html",{"data":data})

def AdminViewProduct(request):
    c.execute("select * from products")
    data = c.fetchall()
    if request.GET:
        st = request.GET.get('st')
        pid = request.GET.get('id')
        if st == 'Accept':
            return HttpResponseRedirect("/AdminUpdateProduct/")
        else:
            c.execute("delete from products where pid = '"+str(pid)+"'")
            db.commit()
    return render(request,"AdminViewProduct.html",{"data":data})

def AdminUpdateProduct(request):
    pid = request.GET.get('id')
    c.execute("select * from products where pid = '"+str(pid)+"'")
    data = c.fetchall()
    if request.POST:
            price=request.POST.get("price")
            qty=request.POST.get("qty") 
            c.execute("update products set pamount = '"+str(price)+"', qty = '"+str(qty)+"' where pid = '"+str(pid)+"'")
            db.commit()
            return HttpResponseRedirect("/AdminViewProduct/")
    return render(request,"AdminUpdateProduct.html",{"data":data})

def subcat(request):
    sublist=[]
    catid=request.GET.get("dataid")
    c.execute("select * from subcategory where catid='"+ str(catid)+"'")
    data2=c.fetchall()
    for d in data2:
        sublist.append(d[2])
    return HttpResponse(json.dumps(sublist),content_type="application/json")

def CustomerAddFeedback(request):
    msg=""
    cid = request.session['cid']
    if request.POST:
        a = request.POST.get('room')
        d = date.today()
        c.execute("insert into feedback(cid,feedback,fdate) values('"+str(cid)+"','"+a+"','"+str(d)+"')")
        db.commit()
        msg = "Your feedback posted successfully"
    return render(request,'CustomerAddFeedback.html',{"msg":msg})

def CustomerSearchProduct(Request):
    s="select * from products"
    c.execute(s)
    data=c.fetchall()
    t="select * from categories"
    c.execute(t)
    data1=c.fetchall()
    s="select * from subcategory"
    c.execute(s)
    data2=c.fetchall()
    e="select * from events"
    c.execute(e)
    data3=c.fetchall()
    return render(Request,'CustomerSearchProduct.html',{"data":data,"data1":data1,"data2":data2,"data3":data3})

def CustomerViewProCategory(Request):
    cname=Request.GET.get("id")
    s="select * from products where catid = '"+str(cname)+"'"
    c.execute(s)
    data=c.fetchall()
    t="select * from categories"
    c.execute(t)
    data1=c.fetchall()
    s="select * from subcategory"
    c.execute(s)
    data2=c.fetchall()
    e="select * from events"
    c.execute(e)
    data3=c.fetchall()
    return render(Request,'CustomerSearchProduct.html',{"data":data,"data1":data1,"data2":data2,"data3":data3})

def CustomerViewProSubCategory(Request):
    sid=Request.GET.get("id")
    s="select * from products where subid = '"+str(sid)+"'"
    c.execute(s)
    data=c.fetchall()
    t="select * from categories"
    c.execute(t)
    data1=c.fetchall()
    s="select * from subcategory"
    c.execute(s)
    data2=c.fetchall()
    e="select * from events"
    c.execute(e)
    data3=c.fetchall()
    return render(Request,'CustomerSearchProduct.html',{"data":data,"data1":data1,"data2":data2,"data3":data3})

def CustomerViewProEvents(Request):
    sid=Request.GET.get("id")
    s="select * from products where subid = '"+str(sid)+"'"
    c.execute(s)
    data=c.fetchall()
    t="select * from categories"
    c.execute(t)
    data1=c.fetchall()
    s="select * from subcategory"
    c.execute(s)
    data2=c.fetchall()
    e="select * from events"
    c.execute(e)
    data3=c.fetchall()
    return render(Request,'CustomerSearchProduct.html',{"data":data,"data1":data1,"data2":data2,"data3":data3})

def CustomerViewProductDetails(Request):
    pid=Request.GET.get("id")
    msg=""
    cid = Request.session['cid']  
    s="select * from products where pid = '"+str(pid)+"'"
    c.execute(s)
    data=c.fetchall()
    t="select * from categories"
    c.execute(t)
    data1=c.fetchall()
    s="select * from subcategory"
    c.execute(s)
    data2=c.fetchall()
    e="select * from events"
    c.execute(e)
    data3=c.fetchall()
    if(Request.POST):
        price = data[0][7]
        qty = Request.POST.get("qty")
        nqty= int(qty)
        c.execute("select qty from products where pid = '"+str(pid)+"'")
        q = c.fetchone()
        cq = q[0]
        if int(nqty) > cq:
            msg = "Invalid Stock"
        else:
            am = int(qty) * int(price)
            c.execute("insert into cart (cid,pid,qty,price)values('"+str(cid)+"','"+str(pid)+"','"+str(qty)+"','"+str(am)+"')")
            db.commit()
            msg = "Order added successfully"
    return render(Request,'CustomerViewProductDetails.html',{"data":data,"data1":data1,"msg":msg,"data2":data2,"data3":data3})

def CustomerOrderProduct(Request):
    pid=Request.GET.get("id")
    s="select * from products where pid = '"+str(pid)+"'"
    c.execute(s)
    data=c.fetchall()
    cid = Request.session["uid"]
    merid = data[0][8]
    price = data[0][6]
    c.execute("insert into cart (cid,fid,pid,amount,qty)values('"+str(cid)+"','"+str(merid)+"','"+str(pid)+"','"+str(price)+"','1')")
    db.commit()
    t="select * from categories"
    c.execute(t)
    data1=c.fetchall()
    u="select * from brands"
    c.execute(u)
    data2=c.fetchall()
    return render(Request,'CustomerViewProDetails.html',{"data":data,"data1":data1,"data2":data2})

def CustomerViewCart(Request):
    cid = Request.session["cid"]
    s="select * from cart inner join products on cart.pid = products.pid where cart.cid = '"+str(cid)+"'"
    c.execute(s)
    data=c.fetchall()
    t="select count(*) from cart where cid = '"+str(cid)+"'"
    c.execute(t)
    data1=c.fetchone()
    u="select sum(price) from cart where cid = '"+str(cid)+"'"
    c.execute(u)
    data2=c.fetchone()
    totalamount = data2[0]
    tot = totalamount
    qt=""
    cqt=""
    nqt=""
    Request.session["pay"] = str(tot)
    if Request.GET:
        ci = Request.GET.get('id')
        c.execute("delete from cart where id = '"+str(ci)+"'")
        db.commit()
        return HttpResponseRedirect("/CustomerViewCart")
    if(Request.POST):
        c.execute("select * from cart where cid = '"+str(cid)+"'")
        data3 = c.fetchall()
        for d3 in data3:
            custid = d3[1]
            proid = d3[2]
            amot = d3[4]
            quty = d3[3]
            carid = d3[0]
            c.execute("insert into customer_order (cid,pid,p_price,p_qty)values('"+str(custid)+"','"+str(proid)+"','"+str(amot)+"','"+str(quty)+"')")
            db.commit()
            c.execute("select qty from products where pid = '"+str(proid)+"'")
            qt=c.fetchone()
            cqt = qt[0]
            nqt = int(cqt) - int(quty)
            c.execute("update products set qty = '"+str(nqt)+"' where pid = '"+str(proid)+"'")
            db.commit()
            c.execute("delete from cart where id = '"+str(carid)+"'")
            db.commit()
        return HttpResponseRedirect("/payment1")
    return render(Request,'CustomerViewCart.html',{"data":data,"data1":data1[0],"data2":data2[0]})

def payment1(request):
    
    if request.POST:
        card=request.POST.get("test")
        request.session["card"]=card
        cardno=request.POST.get("cardno")
        request.session["card_no"]=cardno
        pinno=request.POST.get("pinno")
        request.session["pinno"]=pinno
        return HttpResponseRedirect("/payment2")
    return render(request,"payment1.html")

def payment2(request):
    cno=request.session["card_no"]
    amount=request.session["pay"]
    if request.POST:
        return HttpResponseRedirect("/payment3")
    return render(request,"payment2.html",{"cno":cno,"amount":amount})

def payment3(request):
    return render(request,"payment3.html")

def payment4(request):
    return render(request,"payment4.html")

def payment5(request):
    cno=request.session["card_no"]
    today = date.today()
    name =  request.session['NAME'] 
    amount = request.session["pay"]
    return render(request,"payment5.html",{"cno":cno,"today":today,"name":name,"amount":amount})

def CustomerViewMyBooking(request):
    cid=request.session["cid"]
    c.execute("select * from customer_order inner join products on customer_order.pid = products.pid where customer_order.cid = '"+str(cid)+"'")
    data = c.fetchall()
    return render(request,"CustomerViewMyBooking.html",{"data":data})



