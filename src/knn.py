from numpy import *
import operator
import matplotlib
import matplotlib.pyplot as plt
from utils import *



def createDataSet():
    group=array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels=['A','A','B','B']
    return group,labels




def classify(input,dataset,labels,k):
    datasetsize=dataset.shape[0]
    #print "TI:E, ", tile(input,(datasetsize,1))
    diffmat=tile(input,(datasetsize,1))-dataset
    debug("diffmat ",diffmat)
    sqdiffmat=diffmat**2
    sqdistance=sqdiffmat.sum(axis=1)
    distance=sqdistance**.5
    debug("Distance",distance)
    sorteddistindices=distance.argsort()
    classcount={}
    for i in range(k):
        votelabel=labels[sorteddistindices[i]]
        classcount[votelabel]=classcount.get(votelabel,0)+1
    sortedclasscount=sorted(classcount.iteritems(),key=operator.itemgetter(1),reverse=True)
    return sortedclasscount[0][0]





def file2matrix(filename):
    f=open(filename)
    a=f.readlines()
    numlines=len(a)
    debug("NUmber of lines in the text file :" ,numlines)
    returnMat=zeros((numlines,3))#It creates a 1000x3 matrix filled with zeros
    classvec=[]
    index=0
    for line in a:
        line=line.strip()
        listFromLine=line.split("\t")
        debug("List From Line is ",listFromLine)
        debug("list From line : ",listFromLine[0:3])
        returnMat[index,:]=listFromLine[0:3]
        classvec.append(int(listFromLine[-1]))
        index+=1
    return returnMat,classvec

#datingDataMat,datingLabels=file2matrix("datingTestSet2.txt")
#datingDataMat.min(0)
#a=datingLabels
#b=array(a)
#c=15.0*b
#print c

#fig=plt.figure()
#ax=fig.add_subplot(111)
#ax.scatter(datingDataMat[:,1],datingDataMat[:,2],c,c)
#plt.show()

def autoNorm(dataSet):
    minvals=dataSet.min(0)#returns the minimum value in each column
    maxvals=dataSet.max(0)#returns the maximum value in each column
    
    ranges=maxvals-minvals
    
    normdataset=zeros(shape(dataSet)) 
    m=dataSet.shape[0]
    normdataset=dataSet-tile(minvals,(m,1))
    normdataset=normdataset/tile(ranges,(m,1))
    return normdataset,ranges,minvals



def datingClassTest():
    hoRatio=0.10
    datingDataMat,datingLabels=file2matrix("datingTestSet2.txt")
    normMat,ranges,minVals=autoNorm(datingDataMat)
    m=normMat.shape[0]
    numtestvecs=int(m*hoRatio)
    errorcount=0.0
    for i in range(numtestvecs):
        classifierresult=classify(normMat[i,:],normMat[numtestvecs:m,:],datingLabels[numtestvecs:m],3)
        print "The classifier came back with %d, the real answer is %d" %(classifierresult,datingLabels[i])
        if classifierresult!=datingLabels[i]:
            errorcount+=1.0
    print "The total error rate is : %f " %(errorcount/float(numtestvecs))
    



def classifyPerson():
    resultList=['not at all','in small doses','in large doses']
    percentTats=float(raw_input("percentage of time spent playing video games?"))
    ffMiles=float(raw_input("frequent flier miles earned per year"))
    iceCream=float(raw_input("Liters of ice cream consumed per year"))
    datingDataMat,datingLabels=file2matrix("datingTestSet2.txt")
    normmat,ranges,minvals=autoNorm(datingDataMat)
    inarr=array([ffMiles,percentTats,iceCream])
    classifierResult=classify((inarr-minvals)/ranges,normmat,datingLabels,3)
    print "You will probably like this person" ,resultList[classifierResult-1]
