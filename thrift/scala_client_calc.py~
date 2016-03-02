
import org.apache.thrift.TException;
import org.apache.thrift.transport.TSSLTransportFactory;
import org.apache.thrift.transport.TTransport;
import org.apache.thrift.transport.TSocket;
import org.apache.thrift.transport.TSSLTransportFactory.TSSLTransportParameters;
import org.apache.thrift.protocol.TBinaryProtocol;
import org.apache.thrift.protocol.TProtocol;
import scala_calc_thrift._

object ScalaCalcServer extends App {

	val transport = new TSocket("localhost", 1234);
	transport.open();
	val protocol = new TProtocol.TBinaryProtocol(transport);
	val client = new ScalaCalcService.Client(protocol);
	val sum = client.add(2.0, 3.0);
	System.out.println("2+3=" + sum);
	transport.close();

}
