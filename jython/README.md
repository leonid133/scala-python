install jython
http://www.jython.org/downloads.html

To compile scala_calc.scala
scalac -Xexperimental -cp .:[path]jython.jar scala_calc.scala 

To run PythonCalc
scala -Xexperimental -cp .:[path]jython.jar jython_calc.PythonCalc

