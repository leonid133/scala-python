import org.apache.thrift._
import org.apache.thrift.protocol._
import org.apache.thrift.transport._
import org.apache.thrift.server._
import org.apache.thrift.server.TServer.Args
import scala_calc_thrift._

class ScalaUtilsLogic extends ScalaCalcService.Iface {

 override def add(num1: Double, num2: Double): Double = {
   val addFunction = (num1:Double, num2:Double) => { num1 + num2 }
   addFunction(num1, num2) 
 }
}

 object ScalaCalcServer extends App {
   val serverTransport = new TServerSocket(1234)
   val logic = new ScalaUtilsLogic()
   val processor = new ScalaUtilsService.Processor(logic)
   val plumbing=new Args(serverTransport).processor(processor)
   val server = new TSimpleServer(plumbing)
   println("starting server")
   server.serve();  
 }
