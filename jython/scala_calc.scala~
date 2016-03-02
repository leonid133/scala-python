package jython_calc
import javax.script._
import java.io._

object PythonCalc extends App {
  val scriptEngineManager = new ScriptEngineManager()
  val pyEngine = scriptEngineManager.getEngineByName("python")
  val engine = pyEngine.asInstanceOf[ScriptEngine with Invocable]
  engine.eval(new FileReader("python_calc.py"))
  val a =  2.0.asInstanceOf[AnyRef]
  val b =  3.0.asInstanceOf[AnyRef]
  val pythonAdd  = engine.invokeFunction("py_add", a, b)
  System.out.println(pythonAdd.asInstanceOf[Double].round)
}


