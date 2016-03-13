#Script(DrugA,DrugB,DB)
#iterate throught the db and identify all effects associated with drugA SetA
#iterate throught the db and identify all effects associated with drugb Setb
#iterate throught the db and identify all effects associated with drugA + drugB Setc
#
#output as list events of A+B

setA <- data.frame(Patient = character(0), Effects = character(0), stringsAsFactors = FALSE)
setB <- data.frame(Patient = character(0), Effects = character(0), stringsAsFactors = FALSE)
setC <- data.frame(Patient = character(0), Effects = character(0), stringsAsFactors = FALSE)
#setD <- data.frame(Patient = character(0), Effects = character(0), Coder = character(0), stringsAsFactors = FALSE)

CommonEffectsDB <- function(drugA, drugB, database){
  patients <- database$Patient
  n <- length(patients)
  
  #setA <- data.frame(Patient = integer(0), Effects = (character(0)), stringsAsFactors = FALSE)
  #setB <- data.frame(Patient = integer(0), Effects = (character(0)), stringsAsFactors = FALSE)
  #setC <- data.frame(Patient = integer(0), Effects = (character(0)), stringsAsFactors = FALSE)
  
  for (i in 1:n){
    d <- toString(database$Drugs[i])
    ud <- unlist(strsplit(d,";"))
    
    e <- toString(database$Event[i])
    ue <- unlist(strsplit(e,";"))
    
    p <- toString(patients[i])
    
    #setD[nrow(setD)+1,] <- c(p,e);
    
    if (length(ud) > 1){
      #print (1)
      if(grepl(drugA, ud) || grepl(drugB, ud)) {
        #print (2)
        # consider 1,2; 2,1 cases
        #for (j in 1:length(ud)){
        #  if (is.element(drugA, ud[j]) || is.element(drugB, ud[j])){
        #ue <- unlist(strsplit(e,";"))
        setC[nrow(setC)+1,] <- c(p,toString(ue));
        #setC[nrow(setC)+1,] <- c(p,e);
        #  }
      }
    }
    else{
      #print (3)
      if (drugA %in% d) {
        #print(4)
        setA[nrow(setA)+1,] <- c(p,toString(ue)) # c(p,e)
      }
      
      if (drugB %in% d) {
        #print (5)
        setB[nrow(setB)+1,] <- c(p,toString(ue))
      }
    }
  }
  #setA
  #setB

  #setD
  
  setD <- merge(setA, setB, all = TRUE)
  
  setCp <- do.call("paste", setC)
  setDp <- do.call("paste", setD)
  setC[! setCp %in% setDp, ]
  
  setC
  
  #library(compare)
  #setE <- compare(setD,setC, allowAll=TRUE)
  #setF <- data.frame(lapply(1:ncol(a1),function(i)setdiff(a1[,i],comparison$tM[,i])))
  #setE$tM
}



CommonEffectsMerge <- function (){
  CommonEffectsDB("LETAIRIS","ADCIRCA",test)
  setD <- merge(setA, setB, all = TRUE)
  
  setCp <- do.call("paste", setC)
  setDp <- do.call("paste", setD)
  setC[! setCp %in% setDp, ]
  CommonEffectsDB("LETAIRIS","ADCIRCA",test)
}
#CommonEffects("LETAIRIS","REVATIO",test)
#setC
