from replit import db
#matches = db.prefix("")
#string = """ ,"""
db2={'333716937504980992', '356443870596431874', '398886094005075999', '402073446600802307', '437911312148725771', '438701494120873985', '459960530321276938', '530444913737728010', '537317340660891648', '554743957116944421', '557605314086830090', '568354939340849162', '581523213004046360', '590980034127462413', '614128670700863508', '627817414033276938', '644823032594038825', '663429390469824572', '666972417347944448', '677214856109359118', '683686207460474990', '689015870336663611', '690472529441193984', '693074118450348042', '701896585604497490', '702231289817989291', '703668237761511434', '709683495684931704', '711652552038547537', '717749514785652866', '729985524613382155', '751531315689553920', '761636440836276236', '773410503716241409', '776837823743524874', '777466461886480435', '779887107123839046', '780464306076254295', '781898317146619907', '790677131012866048', '793053803737907211', '797859580477571072', '798799401555460126', '798815015662125056', '799194272263176222', '806917162660790283', '832626436678221874'}
USER=[]
for i in db2:
  try:
    value = db[i]
    print(i + " = " + str(value))
    if int(value) <= 10:
      del db[i]
      print("Silindi")
    else:
      print(i + " = " + str(value))
  except:
    pass

    