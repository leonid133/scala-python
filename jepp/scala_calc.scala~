package jepp_calc

import java.io._
import jep.Jep
import jep.JepException

object PythonCalc extends App {
  
  val jep = new Jep()
  jep.runScript("python_calc.py")
  val a = (2.0).asInstanceOf[AnyRef]
  val b = (3.0).asInstanceOf[AnyRef]
  val pythonCalc = jep.invoke("py_add", a, b)
  println(pythonCalc.asInstanceOf[Float].round)

}
