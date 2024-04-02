package kr.co.aiai.app;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

import java.util.ArrayList;
import java.util.Arrays;

public class MainActivity05 extends AppCompatActivity {

    TextView tv;
    Button btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8,btn9,btn0,btn_call,btn_back;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main05);

        btn0 = findViewById(R.id.btn0);
        btn1 = findViewById(R.id.btn1);
        btn2 = findViewById(R.id.btn2);
        btn3 = findViewById(R.id.btn3);
        btn4 = findViewById(R.id.btn4);
        btn5 = findViewById(R.id.btn5);
        btn6 = findViewById(R.id.btn6);
        btn7 = findViewById(R.id.btn7);
        btn8 = findViewById(R.id.btn8);
        btn9 = findViewById(R.id.btn9);
        btn_call = findViewById(R.id.btn_call);
        btn_back = findViewById(R.id.btn_back);
        tv = findViewById(R.id.tv);

        Button[] btns = {
                btn0,btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8,btn9
        };

        for(Button btn : btns){
            btn.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View view) {
                    click(btn.getText().toString());
                }
            });
        }

        btn_call.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                call();
            }
        });

        btn_back.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                back();
            }
        });
    }

    void click(String text){
        tv.append(text);
    }

    void call(){
        Toast.makeText( this, tv.getText(), Toast.LENGTH_SHORT).show();
    }
    void back(){
        CharSequence str = tv.getText();
        String oldStr = String.valueOf(str);
        String newStr = (oldStr).substring(0,tv.getText().length()-1);
        tv.setText(newStr);
    }

}