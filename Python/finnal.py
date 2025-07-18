def conv(filter, imgarray):
    filh = len(filter)
    filw = len(filter[1])
    featuremap = []

    for a in range(0, (len(imgarray)-filh+1)):
        maprow = []
        for b in range(0, (len(imgarray[1])-filw+1)):
            patchcolumn = []
            for j in range(filh):
                patchrow = []
                for i in range(filw):
                    patchrow.append(imgarray[j][i+b])    

                #print(patchrow)
                patchcolumn.append(patchrow)

            
            neuron = 0
            for j in range(filh):
                for i in range(filw):
                    #print("patch "+ str(patchcolumn[j][i]))
                    #print("filter "+ str(filter[j][i]))
                    neuron = neuron+(patchcolumn[j][i]*filter[j][i])
                    #print("neuron "+ str(neuron))
            maprow.append(neuron)
        #print(maprow)
        featuremap.append(maprow)
    return featuremap