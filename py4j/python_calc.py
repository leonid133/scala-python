from py4j.JavaGateway import JavaGateway

entry_point = JavaGateway().entry_point
scala_calc = entry_point.getScalaCalc()
scala_calc.add(2.0, 3.0)


