
import java.io.File;

import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.NamedNodeMap;
import org.w3c.dom.Node;
import org.w3c.dom.NodeList;
import org.w3c.dom.Text;

public class ReadXmlTest {

	private static void readXml() {
		String path = "file/test-svg.xml";

		File dstfile = new File(path);
		if (!dstfile.exists()) {
			System.err.println("文件不存在：" + path);
			return;
		}

		BaseXML xml = new BaseXML();
		xml.initFromFile(path);

		NodeList nodes = xml.m_root.getElementsByTagName("g"); // 返回"g"节点集合

		//为每一个读入的图层信息建立对应的layerBean对象，设置对象信息
		for (int nk = 0; nk < nodes.getLength(); nk++) {
			Element ele = (Element) nodes.item(nk);
			String id = ele.getAttribute("id");
			System.out.println("id:" + id);
			NodeList childs = ele.getChildNodes();
			if (childs != null && childs.getLength() > 0) {
				System.out.println("childs: " +  childs.getLength());
			}
			getChilds(childs);
		}
	}

	private static void getChilds(NodeList nodes) {
		for (int nk = 0; nk < nodes.getLength(); nk++) {
			Node node = (Node) nodes.item(nk);
			Node next = node.getNextSibling();
			if (!(next instanceof Element)) {
				continue;
			}
			String name = next.getNodeName();
			System.out.println("name: " + name );
			if (next != null) {
				NamedNodeMap map = next.getAttributes();
				if (map != null) {
					for (int i = 0; i < map.getLength(); i++) {
						Node attr = map.item(i);
						name = attr.getNodeName();
						String value = attr.getNodeValue();
						System.out.println("Attribute name: " + name + ", value:" + value);
					}
				}
			}
		}
	}

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		ReadXmlTest.readXml();
	}

}
