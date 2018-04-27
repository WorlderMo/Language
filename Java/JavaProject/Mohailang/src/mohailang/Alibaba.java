package mohailang;

import java.util.*;

public class Alibaba {
    /** 请完成下面这个函数，实现题目要求的功能 **/
    /**
     * 当然，你也可以不按照这个模板来作答，完全按照自己的想法来 ^-^
     **/
    static int solution(int[] machines) {
        int total = 0, avg, step = 0;
        for (int i = 0; i < machines.length; i++) total += machines[i];

        if (total % machines.length != 0) {
            step = -1;
        }else {
            avg = total / machines.length;

            for (int i = 0; i < machines.length - 1; i++)
            {
                if (machines[i] == avg) continue;
                while (machines[i] > avg)
                {
                    machines[i]--;
                    machines[i + 1]++;
                    step++;
                }
                while (machines[i] < avg)
                {
                    if(machines[i]<0)
                        machines[i] = 0;
                    if(machines[i+2]>machines[i+1] && machines[i+1]>machines[i]){
                        machines[i+1]++;
                        machines[i+2]--;
                    }else {
                        machines[i]++;
                        machines[i + 1]--;
                        step++;
                    }
                }
            }
        }
        return step;
    }

    public static void main(String[] args)    //主函数
    {
        Scanner in = new Scanner(System.in);
        int res;
        String[] machinesTmp = in.nextLine().trim().split(",");
        int[] machines = new int[machinesTmp.length];
        for (int i = 0; i < machines.length; i++) {
            machines[i] = Integer.parseInt(machinesTmp[i]);
        }


        res = solution(machines);
        System.out.println(String.valueOf(res));


    }
}