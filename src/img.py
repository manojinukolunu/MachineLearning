from knn import *
from numpy import *
from os import listdir




def img2vector(filename):
    returnvect=zeros((1,1024))
    fr=open(filename)
    for i in range(32):
        linestr=fr.readline()
        for j in range(32):
            returnvect[0,32*i+j]=int(linestr[j])
    return returnvect


def handwrittenclasstest():
    hwLabels=[]
    trainingFileList=listdir('trainingDigits')
    m=len(trainingFileList)
    trainingMat=zeros((m,1024))
    
    for i in range(m):
        fileNameStr=trainingFileList[i]
        fileStr=fileNameStr.split('.')[0]
        debug("File STR :",fileStr)
        classnumstr=int(fileStr.split('_')[0])
        hwLabels.append(classnumstr)
        trainingMat[i,:]=img2vector('trainingDigits/%s'%fileNameStr)
    testFileList=listdir('testDigits')
    errorCount=0.0
    
    mtest=len(testFileList)
    for i in range(mtest):
        fileNameStr=testFileList[i]
        fileStr=fileNameStr.split('.')[0]
        classNumStr=int(fileStr.split('_')[0])
        vectorUnderTest=img2vector('testDigits/%s'%fileNameStr)
        classifierResult=classify(vectorUnderTest,trainingMat,hwLabels,3)
        
        print "the classifier cabe back with %d ,the real answer is : %d"% (classifierResult,classNumStr)
        if (classifierResult!=classNumStr):
            errorCount+=1.0
        
    print "\n the total number of errors is : %d "% errorCount
    print "\n the total error rate is : %f " % (errorCount/float(mtest))
    
handwrittenclasstest()