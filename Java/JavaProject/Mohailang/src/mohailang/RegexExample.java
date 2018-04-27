package mohailang;
import java.util.regex.*;

public class RegexExample{
    public static void main(String[] args) {
        String content = "I am mohailang" + "from China";
        String pattern = ".*mohailang.*";
        boolean isMatch = Pattern.matches(pattern, content);
        System.out.println(" 字符串中是否包含了‘mohailang’字符串？" + isMatch);
}
}
