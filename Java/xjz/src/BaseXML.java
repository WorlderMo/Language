/**
 * Power Control Computer Systems Department
 * Fuchu Operations-Industial And Power Systems & Services
 * Copyright(c) zhxjz
 * 2005 All Rights Reservd.
 *
 * file Name:   BaseXml.java
 * packet Name: pubclass
 *
 * 变更履历
 *   （初版作成） （产品履历编号：）
 *   设计          YYYYMMDD   承认：       调查：       担当：
 *   编码          YYYYMMDD   承认：       调查：       担当：
 *   单体测试       YYYYMMDD    承认：       调查：       担当：
 *
 *   产品履历编号：
 *
 *     承认：        调查：       担当：bzm
 *     变更理由：增加读取int类型的方法
 *
 *
 *
 */
import java.io.File;
import java.util.Hashtable;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.transform.OutputKeys;
import javax.xml.transform.Transformer;
import javax.xml.transform.TransformerFactory;
import javax.xml.transform.dom.DOMSource;
import javax.xml.transform.stream.StreamResult;

import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.Node;
import org.w3c.dom.NodeList;

/**
 * xml操作类.
 *
 * <p>
 * 该类对xml的提供读取和更新功能.
 *
 * @author bzm
 */
public class BaseXML  {
    public BaseXML() {

        try {
            DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
            m_docBuilder = factory.newDocumentBuilder();
        } catch (Exception e) {

        }

    }

    // 共用属性 -------------------------------------------------------
    public DocumentBuilder m_docBuilder = null;

    public Document m_doc = null;

    public String m_strFile = "";

    // 内部属性 -------------------------------------------------------
    public Element m_root = null;

    // 内部方法 -------------------------------------------------------
    // 共用方法 -------------------------------------------------------
    /**
     * 通过文件来初始化xml
     *
     * @param strFileName
     *            文件名称
     */
    public void initFromFile(String strFileName) {
        if (strFileName == null || "".equals(strFileName))
            return;
        try {
            File f = new File(strFileName);
            m_doc = m_docBuilder.parse(f);
            m_root = m_doc.getDocumentElement();
            f = null;
            m_strFile = strFileName;
        } catch (Exception e) {

        }
    }

    /**
     * 从字符串来初始化xml对象
     *
     * @param strXml
     *            xml字符串
     */
    public void initFromStr(String strXml) {
        if (strXml == null || "".equals(strXml))
            return;
        try {
            m_doc = m_docBuilder.parse(strXml);
            m_root = m_doc.getDocumentElement();
        } catch (Exception e) {

        }
    }

    /**
     * 格式化数据
     *
     * @param itName
     *            项目名称
     * @param itVal
     *            项目值
     * @return 返回字符串
     */
    public static String formatItem(String itName, Object itVal) {
        return String.format("<%1$s>%2$s</%1$s>", itName, itVal);
    }
    /**
     * 根据节点名称的得到节点
     *
     * @param strName
     *            节点名称
     * @return 返回节点
     */
    public Node getNodeFromName(Node root, String strName) {
        if (m_root == null)
            return null;
        if (strName == null)
            return null;
        Node node = root.getFirstChild();
        while (node != null) {
            if (strName.compareTo(node.getNodeName()) == 0) {
                return node;
            }
            node = node.getNextSibling();
        }
        return null;
    }
    /**
     * 根据节点名称的得到节点
     *
     * @param strName
     *            节点名称
     * @return 返回节点
     */
    public Node getNodeFromName(String strName) {
        if (m_root == null)
            return null;
        return getNodeFromName(m_root, strName);
    }
    /**
     * 读取xml中一项的内容
     *
     * @param strItemName
     *            项目名称
     * @return 项目的内容
     */
    public String readItem(String strItemName) {
        if (m_root == null)
            return "";
        Node node = getNodeFromName(m_root, strItemName);
        if (node != null)
            return node.getTextContent();
        return "";
    }
    /**
     * 读取子节点
     *
     * @param ndRoot
     *            子节点
     * @param hsNameToVal
     *            子节点名称和值的对应
     */
    public void readItem(Node ndRoot, Hashtable<String, String> hsNameToVal) {
        if (ndRoot == null)
            return;
        NodeList lsNode = ndRoot.getChildNodes();
        int nLen = lsNode.getLength();
        if (nLen == 0)
            return;
        Node node;
        for (int i = 0; i < nLen; i++) {
            node = lsNode.item(i);
            hsNameToVal.put(node.getNodeName(), node.getTextContent());
        }
    }
    /**
     * 读取子节点
     *
     * @param ndRoot
     *            子节点
     * @param strItemName
     *            子节点的下级名称
     * @return 子节点的下级值
     */
    public String readItem(Node ndRoot, String strItemName) {
        if (ndRoot == null)
            return "";
        Node node = getNodeFromName(ndRoot, strItemName);
        if (node != null)
            return node.getTextContent();

        return "";
    }
    /**
     * 读取子节点
     *
     * @param ndRoot
     *            子节点
     * @param strItemName
     *            子节点的下级名称
     * @return 子节点的下级值
     */
    public int readItemToInt(Node ndRoot, String strItemName) {
        if (ndRoot == null)
            return -1;
        Node node = getNodeFromName(ndRoot, strItemName);
        if (node != null)
            return Integer.parseInt(node.getTextContent());
        return -1;
    }
    /**
     * 修改xml项
     *
     * @param strItemName
     *            修改项目
     * @param strItemVal
     *            修改值
     */
    public void updateItem(String strItemName, String strItemVal) {
        if (m_root == null)
            return;
        Node node = getNodeFromName(m_root, strItemName);
        if (node != null)
            node.setTextContent(strItemVal);

    }
    /**
     * 修改子节点
     *
     * @param ndRoot
     *            子节点对象
     * @param strItemName
     *            子节点下级节点名称
     * @param strItemVal
     *            子节点下级节点值
     */
    public void updateItem(Node ndRoot, String strItemName, String strItemVal) {
        if (ndRoot == null)
            return;
        Node node = getNodeFromName(ndRoot, strItemName);
        if (node != null)
            node.setTextContent(strItemVal);
    }

    /**
     * 保存xml文件
     *
     * @return 保存成功返回true 保存失败返回false
     * strEncoder : 编码方式
     */
    public boolean saveXmlToFile(String strEncoder) {
        boolean bRet = true;
        if (m_doc == null)
            return false;
        if ("".equals(m_strFile))
            return false;
        try {
            /** 将document中的内容写入文件中 */
            TransformerFactory tFactory = TransformerFactory.newInstance();
            Transformer transformer = tFactory.newTransformer();
            /** 编码 */
            transformer.setOutputProperty(OutputKeys.ENCODING, strEncoder);
            DOMSource source = new DOMSource(m_doc);
            StreamResult result = new StreamResult(new File(m_strFile));
            transformer.transform(source, result);
            result = null;
            source = null;
        } catch (Exception ex) {
            bRet = false;
        }
        return bRet;
    }
    /**
     * 得到nodelist
     *
     * @param strName
     *            节点名称
     * @return 节点集合
     */
    public NodeList getNodeList(String strName) {
        return m_root.getElementsByTagName(strName);
    }
}
