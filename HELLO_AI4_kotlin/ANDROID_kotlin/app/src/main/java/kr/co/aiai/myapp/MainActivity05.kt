package kr.co.aiai.myapp

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.util.Log
import android.view.View
import android.widget.Button
import android.widget.EditText
import android.widget.TextView
import android.widget.Toast
import java.util.Collections

class MainActivity05 : AppCompatActivity() {

    lateinit var btn0 : Button
    lateinit var btn1 : Button
    lateinit var btn2 : Button
    lateinit var btn3 : Button
    lateinit var btn4 : Button
    lateinit var btn5 : Button
    lateinit var btn6 : Button
    lateinit var btn7 : Button
    lateinit var btn8 : Button
    lateinit var btn9 : Button
    lateinit var btnCall : Button
    lateinit var tv : TextView

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main05)
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
        btnCall = findViewById(R.id.btn_call);
        tv = findViewById(R.id.tv)

        var btns : Array<Button> = arrayOf(btn0,btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8,btn9)
        for( btn:Button in btns){
            btn.setOnClickListener(){
                myClick(btn.text.toString())
            }
        }
        btnCall.setOnClickListener(){
            Toast.makeText(this,tv.text.toString(),Toast.LENGTH_SHORT).show()
        }

//        btn.setOnClickListener(){
//            semClick(it)
//        }
    }

    fun myClick(text:String){
        tv.append(text)
    }

//    fun semClick(v:View){
//        var temp : Button = v as Button
//        var str_new = temp.text.toString()
//        var str_old = tv.text.toString()
//        tv.setText(str_old+str_new)
//    }
}