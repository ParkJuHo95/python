package kr.co.aiai.myapp

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.util.Log
import android.widget.Button
import android.widget.EditText
import android.widget.TextView

class MainActivity03 : AppCompatActivity() {

    lateinit var et_dan : EditText
    lateinit var et_disp  : EditText

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main03)
        val btn = findViewById<Button>(R.id.btn)
        et_dan = findViewById<EditText>(R.id.et_dan);
        et_disp = findViewById<EditText>(R.id.et_disp);

        btn.setOnClickListener(){
            myClick()
        }
    }

    fun myClick(){
        var dan : String = et_dan.text.toString()
        var danNum : Int = dan.toInt()
        var gugu : String = ""
        for (i:Int in 1..9 step 1){
            gugu = gugu + String.format("%d x %d = %d\n", danNum, i, (danNum * i))
        }
        et_disp.setText(gugu)
    }

}