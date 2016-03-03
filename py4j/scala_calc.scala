import py4j.GatewayServer 

object ScalaCalc {

 val add = (a:Double, b:Double):Double => { a + b }

}

object ScalaCalcEntryPoint extends App{

    def getScalaCalc() = ScalaCalc
    var gatewayServer = new GatewayServer(ScalaCalcEntryPoint)
    gatewayServer.start()

}
