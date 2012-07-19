from math import log
import utils


def calculateShanonEnt(dataSet):
    numEntries=len(dataSet)#number of entries in the dataset
    labelCounts={}#creating a dictionary whose values are the values in the final column
    for featureVectors in dataSet:
        currentLabel=featureVectors[-1]
        utils.debug("Current Label "+currentLabel,True)
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel]=0
        labelCounts[currentLabel]+=1
    shanonEnt=0.0
    for key in labelCounts:
        prob=float(labelCounts[key])/numEntries
        utils.debug("Probability for Choosing "+key+":: ",prob,False)
        shanonEnt-=prob*log(prob,2)  #The higher the entropy the more mixed up the data is
    return shanonEnt

def createDataSet():
    dataSet=[[1,1,'yes'],[1,1,'yes'],[1,0,'no'],[0,1,'no'],[0,1,'no'],[0,1,'no']]
    labels=['no surfacing','flippers']
    return dataSet,labels


def splitDataSet(dataSet,axis,value):
    returnDataSet=[]
    for featureVector in dataSet:
        if featureVector[axis]==value:
            reducedFeatureVector=featureVector[:axis]
            reducedFeatureVector.extend(featureVector[axis+1:])
            returnDataSet.append(reducedFeatureVector)
    
    return returnDataSet  


def chooseBestFeatureToSplit(dataSet):
    numFeatures=len(dataSet[0])-1#why this -1?
    baseEntropy=calculateShanonEnt(dataSet)
    bestInfoGain=0.0
    bestFeature=-1
    
    for i in range(numFeatures):
        featList=[example[i] for example in dataSet]
        uniqueVals=set(featList)
        newEntropy=0.0
        for value in uniqueVals:
            subDataSet=splitDataSet(dataSet,i,value)
            prob=len(subDataSet)/float(len(dataSet))
            newEntropy+=prob*calculateShanonEnt(subDataSet)
        infoGain=baseEntropy-newEntropy
        if (infoGain>bestInfoGain):
            bestInfoGain=infoGain
            bestFeature=i
    return bestFeature

            

myDataSet,labels=createDataSet()

myDataSet[0][-1]='maybe'
print myDataSet
print calculateShanonEnt(myDataSet)


